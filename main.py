import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get('SESSION', "BQARoHcx5BtQ_Tmevk8UeP3rGL7dB8zM1x2TwjbchB8KiQzAWyYV8teRNT-x8PV36PKYkeEaZt6ks1CPUSwP2I7NVwiCtxK0gTBJrSJDOS78FeV4mTY6Z-NwOIz34ebhjh92nvcs7vxC7nXYks0Y8io9m5tMzFoDg1iP258OTsX9TWHhgkaxvbWTktoUmNjM4X1X8ygUYoqnYF1GbesRQ8Obvt8E_ohwPuw6JfbBPGFWB2wf1E6PMy1Xsi2En-WaWenNMqnf3dUmVFylHvRTzD6AkIA68CJ32APOgsJqiDGUuyB6GfVGJ-R9eWLL3z9gKDSmaAvRoM2BBnPq9vAmPvn5AAAAAWGbn2gA")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a private bot of @mh_world to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
