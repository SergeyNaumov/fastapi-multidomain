
# Пример того, как импортировать модели из других файлов, чтобы не нагромождать model_list.py
from .models.news import News
from .models.good import Good

# Описание модели "Статьи"
class Article:
  title = "Статьи"
  work_table ='article'
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
      'filedir':'/files/article'
    },
  ]


# Функция, которая затем экпортируется в проект, возвращает словарь 
def get_dict():
  news=News()
  article=Article()
  good=Good()

  return {
    'news': news,
    'article': article,
    'goog':good
  }

model_list=get_dict()
