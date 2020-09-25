# Новости
from .models.news import News
from .models.good import Good
from .models.task import Task

# Статьи
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



def get_dict():
  news=News()
  article=Article()
  good=Good()

  return {
    'news': news,
    'article': article,
    'good':good,
    'task':Task()
  }

model_list=get_dict()
print(model_list)
