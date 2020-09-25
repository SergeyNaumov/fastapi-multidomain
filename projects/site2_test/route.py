from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from lib.engine import cur_engine as s
from lib.database import db
router = APIRouter()

@router.get("/")
async def mainpage():dsksj
  return {'site':'site2'}


