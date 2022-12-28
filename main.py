import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get('SESSION', "BQCNI8vflBhxxHaCZkgZ8BG-iTeVYIywxt3bpNrRkMi9j6JLM0meCsFIsT_rSggSjkGzHcoBTX1lRs3xXAucoChwrqgxV2rihw9L3ldlFz5KhMQw_CbcIwamQ345HilW7PgBhGUDvHewhujZp6Wgp4MWfdt3ADSsibLeRkXs03GA5iLazQ4hTU7_qovczXvCtl9XUaPsTfs1tt3CGDrJxSF__cDUFcqjrySqZ9ixtWgxCeK3p-vKm1hPxfpK9eYCH8PumuCIuBl7CRDJSwcv6r1-2LqAtcdgzM5r-AR33cA7K1iRKwHK_itTb_Qd7EZ5qUuRkNz4_Ira0gFjCbwBRuUEdKn3xAA"
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
