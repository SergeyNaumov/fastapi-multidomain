from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from lib.engine import cur_engine as s
from lib.coresubs import template
router = APIRouter()




@router.get("/", response_class=HTMLResponse)
async def mainpage():
  return template(
    template='./templates/error/500.html',
    vars={
      'error':s.project['error']
    }
  )



