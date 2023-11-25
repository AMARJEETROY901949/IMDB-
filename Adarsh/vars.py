# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '22108471'))
    API_HASH = str(getenv('API_HASH', '4deb56286e89f760d8ec133e52a6e8a5'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6718388339:AAErMhW7Iut_VaR0tdrJtuOxrlcPuISeqig'))
    name = str(getenv('name', 'Fast_Downloader_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002061964415'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5191573246 6250083495").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Expert_botz'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://mongodbuser:mogodbpass@cluster0.appjt7j.mongodb.net/'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'movi_group_hd'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002061964415")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'ziplinker.net')
    SHORTLINK_API = getenv('SHORTLINK_API', 'be4cd844273ae5edebe575dcb14767ed573a3b16')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/movi_group_hd/60')
