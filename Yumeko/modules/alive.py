import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/60f59fda6b2531f276589.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  RIKKA = "**Holla I'm Rikka!** \n\n"
  RIKKA += "×**I'm Working Properly** \n\n"
  RIKKA += "×**My Owner : [Sneha Jha](https://t.me/Sneha_UwU_OwO)** \n\n"
  RIKKA += f"×**Telethon Version : {tlhver}** \n\n"
  RIKKA += f"×**Pyrogram Version : {pyrover}** \n\n"
  RIKKA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Rikka_Tyrant_bot?start=help"), Button.url("Support", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=RIKKA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  RIKKA = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=RIKKA,  buttons=BUTTON)
