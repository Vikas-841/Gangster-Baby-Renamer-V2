import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "BQGKEwAAcEXua7wbIvc4-o5vPpvaumwk2X66LghxEwnpWjazg8mXhlnBmVjFov7Bgy8-Lw9ApO-juV8jQNWJFg5Vzai5BShhxhxEEmCwmIiEtuoHQsjCGT7kbzwpV6zqLGM_vIfH_4wFD50hHwOXAElTH1ly6xXDxJZP00DU4CdR7FJO4c5Yt-f50FrQ_Qa4Ed-R9isnQ0hGqJIvmhJ0J2A2HKO9jvY6xgHBH03KHS5SJCMBralkNtRrmikSZ2Pmotm8VYWClK-CRLGoUlnJk3Vu-ZiY2kg1dvrX0wa3bDzqlcSbD2pyk3tGfJwWUB8aTjYqX3aWFyuY7lof6IYJMYJYizZLlwAAAAGW8Ud6AA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
