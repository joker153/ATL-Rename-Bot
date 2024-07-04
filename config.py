import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "6119632")
API_HASH = os.environ.get("API_HASH", "5b51582f938e93c8eab32612d5045737")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "6426072097:AAFpvNEzW65qVT6XwTxzafDLJKFk-Xtbun0")

CHANNEL = os.environ.get("CHANNEL", "") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","")
STRING = os.environ.get("STRING", "1BVtsOJ4Bu4p5EEnU5dLWCWl-nE9yste6vR_44tFWlySK5i_IwC9vG_Bue7bELVb16EEwnSTZMKlNm7MsaPtt2YE-5_rD8cZAX6Up9-gc8CGzHg0-Bh5-3H0PcfWPNYoSMFXpR-InAHBbYcU8u31pfunIXhhtRYaSg3f0mgabLw9uKFnKXT7WOv1NKxwl0iO83xMntzMxvs0eSyuG_YP5A0cHT1_DNTAZfKjZ2kLN9ek-W3-6Tn0I9CVXQrPINMDiWrVXSGP_1nahadWiG8Nwpy7Z3-SK3Gn77BT0_XvnLqc0aNE0NrjPc6uAdvqwod_uVBIiSVqPEXdsWlagZ7Q_bqG097M27UQ=")

DB_NAME = os.environ.get("DB_NAME","renam")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://amal:amal@cluster0.6qbjqaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

FLOOD = int(os.environ.get("FLOOD", "0"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1989750989').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002049486679"))
