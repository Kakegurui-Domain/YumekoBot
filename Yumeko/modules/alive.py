import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YumekoBot.events import register as MEMEK
from YumekoBot import telethn as tbot

PHOTO = "https://telegra.ph/file/7c3c26e0ed938aec91209.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Holla I'm Luna!** \n\n"
  YUMEKO += "🔴 **I'm Working Properly** \n\n"
  YUMEKO += "🔴 **My Master : [zeinzo](https://t.me/tdrki_1)** \n\n"
  YUMEKO += f"🔴 **Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/lunatapibot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/lunaXresso")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/zeinproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
