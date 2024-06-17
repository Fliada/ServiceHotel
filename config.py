from db_helper.DBHelper import *
from local_settings import postresql as settings

keys = ["pguser", "pgpasswd", "pghost", "pgport", "pgdb"]
if not all(key in keys for key in settings.keys()):
    raise Exception("Bad confid file")

helper = DBHelper(
    settings["pguser"],
    settings["pgpasswd"],
    settings["pghost"],
    settings["pgport"],
    settings["pgdb"],
)