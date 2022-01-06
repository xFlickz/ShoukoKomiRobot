"""
This Bot Was Developed By The Owner Of @StrawHat_Network.
Join his network and support him.
"""
from pyrogram import Client
from pyrogram.types import CallbackQuery

from SmartConverter.Plugins.converter import *
from SmartConverter.translation import Translation

from SmartConverter.Plugins.cb import *

@TGBot.on_message(filters.command("start", prefixes=["/", "."]))
async def start_cmd_handler(bot, message):
  await message.reply_video(
    video="https://telegra.ph/file/d344fcd1367121197eccc.mp4",
    caption=Translation.START_TEXT,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙷𝙴𝙻𝙿✫", callback_data="help"),
          InlineKeyboardButton("✫𝙰𝙱𝙾𝚄𝚃✫", callback_data="about")
        ],
        [
          InlineKeyboardButton("✫𝙽𝙴𝚃𝚆𝙾𝚁𝙺✫", url="http://t.me/StrawHat_Network")
        ],
      ],
    ),
    parse_mode="md",
    quote=True
  )
  
@TGBot.on_callback_query()
async def c_b(bot, update):
  if update.data == "help":
    await help_message(bot, update)
  elif update.data == "about":
    await about_message(bot, update)
  elif update.data == "back":
    await back_message(bot, update)