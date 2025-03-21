from pydal import Field, DAL
from config import HOSTDB

database = DAL(dbinfo, db_codec='UTF-8',
               folder=dbfolder,
               fake_migrate=True,
               migrate=True,
               pool_size=1)
