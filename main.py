from fastapi import Depends, FastAPI, Response, Header, Request #, Form, File, UploadFile
from fastapi import FastAPI, APIRouter
from lib.get_sites import sites
from lib.engine import cur_engine as s
from lib.config import multisites
# uvicorn main:app --reload --port=5010

app = FastAPI(Debug=True)

prev_domain='';
# ==================================================
# Здесь можно на выбор сделать тот режим, в котором приложение будет работать
# Если нужно обрабатывать много доменов одним приложением
# ==================================================


# multidomains:
@app.middleware("http")
async def for_all_requests(request: Request,call_next):
  global prev_domain,routers
  if multisites:
      host=request.headers['host']
      print('host:',host)
      if prev_domain !=host:
          app.routes.clear()
          
          if host in sites:
            project=sites[host]['project']
            error=project['error']
            if error: # выводим ошибку
              response = Response(error, media_type='text/html')
              return response
            else:
              local_response=s.set_project(request,project)
              if local_response:
                return local_response

              else:
                app.include_router(sites[host]['router'], prefix="")
                response = await call_next(request)
                return response

            prev_domain=host
          else:
            return Response('domain: '+host+' not found',media_type='text/html')

  #else: # onedomain
      #app.include_router(router, prefix="")
      # /onedomain
  







