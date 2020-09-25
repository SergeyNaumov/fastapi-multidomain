from fastapi import FastAPI, APIRouter,Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from lib.engine import cur_engine as s



router = APIRouter()

# Страница "Формы"
@router.get('/',response_class=HTMLResponse)
def page_forms():
  if s.param('debug'):
    model_news=s.project['models']['news']

    return str(model_news)
  s.to_tmpl('page_type','forms')
  return s.out_template()

# обработчик формы (без ajax)
@router.post('/task-without-ajax')
def add_task_without_ajax(
    header: str = Form(...), body: str = Form(...), priority: str = Form(...)
):
  

  return s.get_form(
    model='task',
    use_capcha=1,
    mail_send=[
      {
        'to': 'svcomplex@gmail.com',
        'subject':'новая задача',
        'message':'текст письма'
      }
    ],
    data={'header':header,'body':body,'priority':priority},
    # fields=[
    #   {
        
    #     'type':'text',
    #     'name':'header',
    #     'regexp_rules':[
    #         '.+','Поле не должно быть пустым',
    #         #'^.{1,6}$','Не более 6-ти символов',
    #         #'/^[0-9]+$/','Только цифры',
    #     ]
    #   },
    #   {
    #     'name':'body',
    #     'type':'text',
    #     'regexp_rules':[
    #         '.+','Поле не должно быть пустым',
    #     ]
    #   },
    #   {
    #     'name':'priority',
    #     'type':'checkbox',
    #   },
    # ]
  )
# create table struct_1_task(
#    id int primary key auto_increment,
#    header varchar(255) not null default '',
#    registered timestamp default current_timestamp,
#    date_to date,
#    body text
#  ) engine=innodb default charset=utf8;

# обработчик формы (с ajax)
@router.post('/task-with-ajax')
def add_task_without_ajax():
  return s.get_form(model='task')

