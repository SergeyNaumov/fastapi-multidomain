from re import *

def exists_arg(key,dict):
  if (key in dict) and dict[key]:
    return True
  return False

def get_model(s,model_name):
  models=s.project['models']
  if exists_arg(model_name,models):
    return models[model_name]

  
  #s.project.error='Структура '+model_name+'не найдена'
  return None


# Проверяем форму
def check_form(s,arg):
  #global model
  fields=[]
  errors=[]
  errors_for_fields={}
  data_result={}
  if not exists_arg('model',arg ):
    #s['error']=
    errors.append('для get_form не указан параметр model_name')
  else:
    model_name=arg['model']
    model=get_model(s,model_name)
    if not model:
      errors.append('Модель '+model_name+' не найдена в проекте')

  if exists_arg('action_field',arg ):
    action_field=arg['action_field']

  if exists_arg('action_field',arg ):
    action_field_value=arg['action_field_value']

  if not exists_arg('data',arg):
    errors.append('not set attr data for get_form')

  
  
  if exists_arg('fields',arg):
    fields=arg['fields']
  else:
    fields=model.fields

  if not len(fields):
    errors.append('массив fields пуст')
  else:
    for f in fields:
      value=None
      if exists_arg(f['name'],arg['data']):
        value=arg['data'][f['name']]
      
      print(f['name'],'/',f['type'],'/',value)
      if exists_arg('type',f):
        if(f['type']=='checkbox'):
          if(value): value=1
          else: value=0
          
          print(f['name'],'/',f['type'],'/',value)
      if not(value == None):

        # Нужно ли проверять регулярками?
        if exists_arg('regexp_rules',f):
          i=0
          while i<len(f['regexp_rules']):
            regexp=f['regexp_rules'][i]
            error_message=f['regexp_rules'][i+1]
            
            pattern = compile(regexp)
            if not pattern.match(value):
              errors.append(error_message)
              if not exists_arg(f['name'],errors_for_fields):
                errors_for_fields[f['name']]=[]

              errors_for_fields[f['name']].append(error_message)
            i+=2

        data_result[f['name']]=value
  
  return errors, errors_for_fields, model,fields,data_result


def get_form(s,arg):

  # Ответ:
  # {
  #   success:[0,1],
  #   errors:[...],
  #   record_id:[число, в случае, если мы успешно добавили запись в базу]
  # }

  #action_field='action'
  result={}
  errors,errors_for_fields, model,fields,data_result = check_form(s,arg)
  
  #result['fields']=fields

  if not len(errors): # ошибок нет, обрабатываем форму
    arg['table']=model.work_table
    result['success']=1
  else:
    result['success']=0

  result['data_result']=data_result
  result['errors_for_fields']=errors_for_fields
  result['errors']=errors
  arg['result']=result
  if result['success']: # всё в порядке, выполняем запрос
    form_id=s.db.save(
      table=arg['table'],
      data=data_result
    )

    if s.db.error_str: # произошла ошибка при выполнении запроса
      print(s.db.error_str)
      errors.append(s.db.error_str)

    result['form_id']=form_id


# create struct_1_task(
#   id int primary key auto_increment,
#   header varchar(255) not null default '',

# );

  return result