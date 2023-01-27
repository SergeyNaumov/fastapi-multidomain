from fastapi import Response
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError
from .database import db
from .dbl.get_data import get_data as gd
from .dbl.get_form import get_form as gf
import urllib.parse
import os.path
import json

def exists_arg(key,dict):
  if (key in dict) and dict[key]:
    return True
  return False


def get_env(request):
  env={'headers':{}}
  for v in ['method','path']: # 
    env[v]=request[v]
  for v in ['query_string']:
    env[v]=urllib.parse.unquote(request[v].decode('utf-8'))
  for h in request['headers']:
    name=h[0].decode('utf-8')
    value=h[1].decode('utf-8')
    env['headers'][name]=str(value)
  return env



def template(**arg):
  dir,template=split_full_path(arg['template'])
  output=''
  env = Environment(loader=FileSystemLoader(dir))
  tmpl = env.get_template(template)
  output=tmpl.render(**arg['vars'])
  return output


def split_full_path(full_path):
  list = full_path.split('/')
  template=list.pop()
  dir='/'.join(list)
  return dir,template


class Engine():
  def __init__(self,**arg):
    if exists_arg('is_multisite','arg'):
      self.is_multisite=True
    else:
      self.is_multisite=False

    self.vars={}
    if exists_arg('template_folder','arg'): self.template_folder=arg['template_folder']
    else: self.template_folder='./templates'
    
    
    
    self.db=db
    
    # main_template
    if exists_arg('main_template','arg'):
      self.main_template=arg['main_template']
    else:
      self.main_template='index.html'
  
  def to_json(self,data,formatted=None):
    if formatted:
      return json.dumps(data, sort_keys=False,indent=2,ensure_ascii=False,separators=(',', ': '))
    else:
      return json.dumps(data, sort_keys=False,ensure_ascii=False,separators=(',', ': '))

  def param(self,par_name):
    for para in self.env['query_string'].split('&'):
      if para:
        split_para=para.split('=')
        if len(split_para)==2:
          name,value=split_para
          if(name==par_name): return value
    return None
      

  def to_tmpl(self,*arg):
    if len(arg) == 2:
      self.vars[arg[0]]=arg[1]

  def set_project(self,request,project):
    self.project=project
    self.vars={}
    self.env=get_env(request)
    if ('start' in project) and project['start']:

      response=project['start']()
      if response: return response


    def tmpl_saver(name,value):
      self.vars[name]=value

    self.db.set_tmpl_saver(tmpl_saver)
    if project['folder']:
      self.template_folder='./templates/'+project['folder']
    else:
      self.template_folder='./projects/'+project['module_folder']+'/templates/'
    


  def set_template_folder(self,new_folder):
    template_folder=new_folder

  def get_promo(self):
    print('promo:')

  def out_template(self):
    out=''
    if hasattr(self,'error') and self.error:
      return self.error

    full_path=self.template_folder + '/' +self.main_template
    print('full_path:',full_path)
    if( not os.path.isfile(full_path)):
      return 'file not found: ' + full_path
    
    try:
      out=template(template=full_path,vars=self.vars)
    except Exception as e:
      out='Error in ' + self.template_folder + '/' + str(e)
      
    return out

  def get_data(self, **arg):
    return gd(self,arg)
  
  def get_form(self,**arg):
    return gf(self,arg)

cur_engine=Engine(is_multisite=True)