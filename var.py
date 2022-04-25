from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", None)
    TELETHON_ID = config("TELETHON_ID", "1AZWarzwBuxuU-AWQctktFInqpum4JIzVJaYSyKEVoxSZZSpXLTA-0LRbktoHCXz5mOQrEOLZanwdi4OBJgwKy-XmHyhQPqU1VJzxg2Co58N0MP-Ignrc7XJunTXPGCO2Zd7Zh0UchllrAP8fz1gja_5MxeARMMlEIWkS_hnVXyfbRBMGHVbPl3yADDq-ztoVbACFp9d-DeUhTFNx6I2MKBLDPW8ZyidH972lUiWZLynJmFs7kJwdy5jWGBeNRpX5LCOU2vgnA6TPMV5qHd6hX47DMBT5isUXyHYtiujNbMs1aS67Cg9UpI0avZgLPAIAYMvdUirnTo7pIiGLeaVvTZIOA4dnjcs=")
    SUDO = list(map(int, getenv("SUDO").split()))
