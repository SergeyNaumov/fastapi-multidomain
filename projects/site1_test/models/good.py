class Good:
  title = 'Товары'
  work_table = 'struct_1_news'
  work_table_id = 'id'
  in_ext_url = True
  
  fields=[
    {
      'description':'Наименование товара',
      'type':'text',
      'name':'header'
    },
    {
      'description':'Артикул',
      'type':'text',
      'name':'anons'
    },
    {
      'description':'Цена',
      'type':'text',
      'name':'price',
      'regexp':'^\d+$'
    },
    
  ]