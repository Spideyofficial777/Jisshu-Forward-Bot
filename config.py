# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28519661")
    API_HASH = environ.get("API_HASH", "d47c74c8a596fd3048955b322304109d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5518489725').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://vebop71691:GtrOdO2tT8v6Yh9q@cluster0.bep2m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002294764885'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002470391435") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
