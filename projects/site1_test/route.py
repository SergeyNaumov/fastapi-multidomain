from fastapi import FastAPI, APIRouter,Response, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from lib.engine import cur_engine as s
from .form_routes import router as form_routes
from lib.capcha import capcha_router

router = APIRouter()
out=''
router.include_router(form_routes, prefix="/forms")
router.include_router(capcha_router, prefix="")

# выполняется в первую очередь
def start():
  # if(s.param('debug')):
  #   return Response(
  #     'debug: '+s.param('debug'),
  #     media_type='text/html', #response.media_type
  #     headers={'computer':'ZX Spectrum 48k'}
  #   );
  
  s.vars['capcha_settings']={
    'text_position':(5, 5),
    'noise_level':30,
    'width':100,
    'height':40,
    'bg_color':(255,255,255,255),
    'font_color':'#000000',
    'font_size':25,
  }

  # показываем информацию о проекте
  if(s.param('show_project')):
    print(str(s.project))
    return Response(
      str(s.project),
      media_type='text/html'#response.media_type
    );

  # показываем env
  if(s.param('show_env')):
    return Response(
      s.to_json(s.env,1),
      media_type='application/json'#response.media_type
    );

  # редирект
  if(s.param('redirect')):
    return RedirectResponse(
      'https://ya.ru',
      headers={'status':'301'}
    )

@router.get('/ajax/city')
def ajax_city():
  return [
    {'id':1,'name':'Москва'},
    {'id':2,'name':'Краснодар'},
    {'id':2,'name':'Сочи'},
  ]

# Тестирование записи в базу
@router.get("/test-save-db")
def test_save_db():
  s.db.query(
    query='truncate for_test_save',
  )

  s.db.save(
    table='for_test_save',
    data={
      'header':'тестовый заголовок',
      'dt':'2020-09-23 15:33:22',
      'd':'2020-09-23',
      'type':'3'
    }
  )



  result=s.db.getrow(
    table='for_test_save'
  )

  return result


@router.get("/",response_class=HTMLResponse)
def mainpage():
  #start()
  s.to_tmpl('page_type','main')
  
  # s.get_data(
  #   debug=1,
  #   struct='news',
  #   order='id desc',
  #   to_tmpl='last_news'
  # )
  return s.out_template()

# Страница "Модели"
@router.get('/models',response_class=HTMLResponse)
def page_models():
  s.to_tmpl('page_type','models')
  return s.out_template()



@router.get("/zztop")
def zztop():
  return s.param('a')

# Обработка 404-й ошибки
@router.get('/{path:path}')
async def page_404(path):
    #raise HTTPException(status_code=400, detail='Bad request')
    s.to_tmpl('page_type','404')
    return Response(
       s.out_template(),
       media_type='text/html', #response.media_type
       headers={'computer':'ZX Spectrum 48k'}
    );




