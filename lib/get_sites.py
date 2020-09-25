from lib.database import db
import importlib
from projects.error_route import router as router_error

def get_sites():
  # import of routers for all sites
  sites_hash={}

  sites=db.get(
    select_fields='wt.domain, t.folder, wt.project_id',
    table='domain',
    tables=[
      {'t':'project','a':'p','l':'wt.project_id = p.project_id'},
      {'t':'template','a':'t','l':'wt.template_id = t.template_id'},
    ],
  )
   
  for item in sites:
      router=''
      error=''
      start=''
      models_project=None
      try:
          #print('load_struct: projects.'+item['folder']+'.structs')
          module_name='projects.'+item['folder']+'.model_list'
          module = importlib.import_module(module_name)
          models=module.model_list
      except Exception as err:
          models={}
          error= item['folder'] + ': '+str(err)



      if error:
        router=router_error
      else:
        try:
            module_name='projects.'+item['folder']+'.route'
            module = importlib.import_module(module_name)
            router=module.router
            start=module.start

            #print('d:',item['domain'],'start',start)

        except Exception as err:
            router=router_error
            error='Error load module '+module_name+': '+str(err)
      




      sites_hash[item['domain']] = {
        'router':router,

        'project':{
            'id':item['project_id'],
            'domain':item['domain'],
            'start':start,
            'folder':item['folder'],
            'models':models,
            'error':error,
        }
      }

  return sites_hash


sites=get_sites()