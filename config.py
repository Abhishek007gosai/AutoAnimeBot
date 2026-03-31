from os import getenv
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()

LOGS = logging.getLogger(__name__)

class Var:
    API_ID = int(getenv("API_ID", "29245477"))
    API_HASH = getenv("API_HASH", "0abc83883262245c90ca337b7a0375c4")
    BOT_TOKEN = getenv("BOT_TOKEN", "7686806902:AAGxlvsZGrOHCXPbS6qV3X_hJzr7VlrzwC8")

    # ✅ FIXED (important)
    DB_URI = getenv("DB_URI", "mongodb+srv://Kafka:Au3OoWzCDYJKeuHU@cluster0.lz2m8iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = getenv("DB_NAME", "cluster0")

    BAN_SUPPORT = getenv("BAN_SUPPORT", "https://t.me/EternalsHelplineBot")
    FSUB_LINK_EXPIRY = int(getenv("FSUB_LINK_EXPIRY", "120"))

    CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003568472008"))
    MHCHANNEL_URL = getenv("MHCHANNEL_URL", "https://t.me/+t0weAQsq_-1lYmJl")

    ANIME = getenv("ANIME", "Is It Wrong to Try to Pick Up Girls in a Dungeon?")
    CUSTOM_BANNER = getenv("CUSTOM_BANNER", "https://ibb.co/5xjBCXKp")

    PROTECT_CONTENT = getenv("PROTECT_CONTENT", "False").lower() == "true"

    BACKUP_CHANNEL = int(getenv("BACKUP_CHANNEL", "-1003874984159"))
    LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1002456565415"))
    MAIN_CHANNEL = int(getenv("MAIN_CHANNEL", "-1003587010814"))
    FILE_STORE = int(getenv("FILE_STORE", "-1002456565415"))

    ADMINS = list(map(int, getenv("ADMINS", "8786691721").split()))

    RSS_ITEMS = getenv("RSS_ITEMS", "https://subsplease.org/rss/?r=1080").split()
    SEND_SCHEDULE = getenv("SEND_SCHEDULE", "True").lower() == "true"

    BRAND_UNAME = getenv("BRAND_UNAME", "")

    FFCODE_1080 = getenv("FFCODE_1080")
    FFCODE_720 = getenv("FFCODE_720")
    FFCODE_480 = getenv("FFCODE_480")
    FFCODE_360 = getenv("FFCODE_360")
    FFCODE_HDRip = getenv("FFCODE_HDRip")

    QUALS = getenv("QUALS", "480 720 1080 HDRip").split()

    DISABLE_CHANNEL_BUTTON = getenv("DISABLE_CHANNEL_BUTTON", "False").lower() == "true"
    AS_DOC = getenv("AS_DOC", "True").lower() == "true"

    THUMB = getenv("THUMB")
    START_PIC = getenv("START_PIC", "https://ibb.co/5xjBCXKp")
    FORCE_PIC = getenv("FORCE_PIC", "https://ibb.co/5xjBCXKp")


# ✅ Required variable validation
REQUIRED_VARS = ["API_ID", "API_HASH", "BOT_TOKEN", "DB_URI"]

for var_name in REQUIRED_VARS:
    if not getattr(Var, var_name):
        LOGS.critical(f"Missing required environment variable: {var_name}")
        exit(1)


# ✅ Logging Setup
LOG_FILE_NAME = "log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
