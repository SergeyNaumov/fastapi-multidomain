
def exists_arg(key,dict):
  if (key in dict) and dict[key]:
    return True
  return False


def modify_case_field(field):

  if exists_arg('values',field) and len(field['values']):
    name=str(field['name'])
    arr=['CASE']
    for item in field['values']:
      arr.append('WHEN wt.'+name + '= "' + str(item['v']) +'" THEN "' + str(item['d']) + '"' ) 

    arr.append('END as '+name+'_formatted')
    return ' '.join(arr)
  else:
    return ''
  


def get_model(s,model_name):
  models=s.project['models']
  if exists_arg(model_name,models):
    return models[model_name]

  s.project.error='Структура '+model_name+'не найдена'
  return None

def normalize(model,arg):

  if not exists_arg('select_fields',arg):
    # если нет select_fields
    arr_select_fields=[str(model.work_table_id) ]

    for f in model.fields:
      _type=str(f['type'])
      _name=str(f['name'])
      if _type == 'file':
        print('file: ',_name)

      elif _type == 'select_values':
        fld=modify_case_field(f)
        if fld:
          arr_select_fields.append(str(fld) )
        
      elif (_type == 'date' or _type=='datetime') and exists_arg('format',f) :
        
        fld='DATE_FORMAT(wt.' + str(_name) + ", '"+str(f['format']) +"') " + str(_name) + '_formatted'
        
        arr_select_fields.append(str(fld) )
      else:
        arr_select_fields.append('wt.' + _name)
    
    new_select_fields=','.join(arr_select_fields)
    
    #print("select_fields:", new_select_fields )

    arg['select_fields']=','.join(arr_select_fields)


  return ''



def get_data(s,arg):
  project=s.project

  if exists_arg('struct', arg):
    model_name=arg['struct']
    model=get_model(s,model_name)
    normalize(model,arg)
    arg['table']=model.work_table
    


    result=s.db.get( **arg )
    # if s.db['err_str']:
    #   s.error=s.db.err_str
    #   print('error_str: ', s.error )
      

    return result
    #else:
    #  project.error='В структуре '+struct_name+' отсутствует параметр work_table'
    #  return ''
  return 'XX'