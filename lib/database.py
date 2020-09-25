from .dbl.freshdb import FreshDB
from .config import database_name,database_host,database_password,database_user
def connect():
  return FreshDB(dbname=database_name,user=database_user,host=database_host,password=database_password)

db=connect()
db.query(query="set lc_time_names = 'ru_RU'")