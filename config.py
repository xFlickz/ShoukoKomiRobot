import os
import dotenv


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  DOWNLOAD_LOCATION = "./temp"   

Config.AUTH_USERS = -1001782235504, 1666551439, 1930343434

Config.API_ID = 3281305
Config.API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
Config.BOT_TOKEN = "5047582631:AAFNGWslp7Rwohq_wyMtzqQktotTR2HL-lQ"