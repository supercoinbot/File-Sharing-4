import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6335578763:AAE6kcwCTqhZvzzJ-Wi9P2nnDfye4T6CGmg")

APP_ID = int(os.environ.get("APP_ID", "29984264"))

API_HASH = os.environ.get("API_HASH", "446a0cb9435771db57048243476ae517")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001724724124"))

OWNER_ID = int(os.environ.get("OWNER_ID", "1368154988"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get("START_MESSAGE", "Привет {firstname}\n\nI помогу создать приватную ссылку на файлы для твоего канала")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Ваш список администраторов не содержит допустимых целых чисел.")

ADMINS.append(OWNER_ID)
ADMINS.append(1368154988)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
