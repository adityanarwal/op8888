from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", None)
    TELETHON_ID = config("TELETHON_ID", None)
    SUDO = list(map(int, getenv("SUDO").split()))
