class News:
  title = 'Новости'
  work_table = 'struct_1_news'
  work_table_id = 'id'
  in_ext_url = True
  
  fields=[
    {
      'description':'Наименование новости',
      'type':'text',
      'name':'header'
    },
    {
      'description':'Анонс',
      'type':'textarea',
      'name':'anons'
    },
    {
      'description':'Текст новости',
      'type':'wysiwyg',
      'name':'anons'
    },
    {
      'description':'Фото',
      'type':'file',
      'name':'photo',
      'filedir':'/files/news',
      'resize':[
        {
          'description':'Горизонтальное фото',
          'file':'<%filename_without_ext%>_mini2.<%ext%>',
          'size':'1004x490',
          'quality':'90'
        },
        {
          'description':'Вертикальное фото',
          'file':'<%filename_without_ext%>_mini1.<%ext%>',
          'size':'488x1008',
          'quality':'95'
        },
        {
          'description':'Квадратное фото',
          'file':'<%filename_without_ext%>_mini3.<%ext%>',
          'size':'500x500',
          'quality':'95'
        },
        {
          'description':'Фото для страницы статьи',
          'file':'<%filename_without_ext%>_mini4.<%ext%>',
          'size':'1165x672',
          'quality':'90'
        },
      ]

    },
    {
      'description':'Дата и время добавления',
      'type':'datetime',
      'name':'registered',
      'format':"%%e %%M %%Y"
    },
    {
      'description':'Тип новости',
      'type':'select_values',
      'name':'type',
      'values':[
        {'v':'1','d':'новость'},
        {'v':'2','d':'статья'},
        {'v':'3','d':'аналитический обзор'}
      ]
    }
  ]