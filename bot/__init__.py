from pyrogram import Client
from requests import get
from bot.config import *

ixel = Client(
  name = "ixel",
  api_id = API_ID,
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  workers = 24,
  sleep_threshold = 60
)

url = "https://ixelator.herokuapp.com/api"
r = get(url)
data = r.json()


for file, content in data.items():
  with open(f"bot/modules/{file}.py", "w") as f:
    f.write(content)
  print(file, "Plugini Yüklendi!")
ixel.plugins = dict(root="ixelator/modules")
