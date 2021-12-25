import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/7c3c26e0ed938aec91209.jpg"

@MEMEK(pattern=("/mhelp"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "** ──「 Basic Guide 」── ** \n\n"
  YUMEKO += "• /play **(song title) — To Play the song you requested via YouTube** \n"
  YUMEKO += "• /search ** (song/video title) – To search for links on YouTube with details** \n"
  YUMEKO += "• /playlist - **show the list song in queue** \n"
  YUMEKO += "•/lyric - ** (song name) lyrics scrapper** \n\n"
  YUMEKO += "** ──「 Admin CMD 」── ** \n\n"
  YUMEKO += "• /pause - **To Pause Song playback** \n"
  YUMEKO += "• /resume - **To resume playback of the paused Song** \n"
  YUMEKO += "• /skip - **To Skip playback of the song to the next Song** \n"
  YUMEKO += "• /end - **To Stop Song playback** \n"
  YUMEKO += "• /control - **open the player settings panel** \n"
  YUMEKO += "• /reload - **To Refresh admin list** \n"

  BUTTON = [[Button.url("☎️ Support", "https://t.me/lunaXresso"), Button.url("📡 Updates", "https://t.me/ZeinzoProject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
