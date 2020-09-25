from fastapi import FastAPI, APIRouter,Response, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from lib.engine import cur_engine as s
from .form_routes import router as form_routes


router = APIRouter()
out=''

# выполняется в первую очередь
def start():
if(s.param('debug')):
    return Response(
        'debug: '+s.param('debug'),
        media_type='text/html', 
        headers={'computer':'ZX Spectrum 48k'} # выводим произвольные заголовки
    );

# показываем информацию о проекте
if(s.param('show_project')):
    print(str(s.project))
    return Response(
        str(s.project),
        media_type='text/html'
    );

# показываем env (переменные окружения проекта)
if(s.param('show_env')):
    return Response(
        s.to_json(s.env,1),
        media_type='application/json'
    );

# редирект
if(s.param('redirect')):
    return RedirectResponse(
    'https://ya.ru',
    headers={'status':'301'}
    )

# Пример контроллера для возврата json-данных
@router.get('/ajax/city')
def ajax_city():
return [
    {'id':1,'name':'Москва'},
    {'id':2,'name':'Краснодар'},
    {'id':2,'name':'Сочи'},
]

# Пример записи в базу данных и получения результата
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
s.to_tmpl('name','Вася')
s.get_data(
    debug=1,
    struct='news',
    order='id desc',
    to_tmpl='last_news'
)
return s.out_template()

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
    );




