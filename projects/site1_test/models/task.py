class Task:
  title = 'Задачи'
  work_table = 'struct_1_task'
  work_table_id = 'id'
  in_ext_url = True
  fields=[
    {
      'description':'Наименование задачи',
      'type':'text',
      'name':'header'
    },
    {
      'description':'Подробное описание',
      'type':'textarea',
      'name':'body'
    },
  ]