"""
This Bot Was Developed By The Owner Of @StrawHat_Network.
Join his network and support him.
"""

from pyrogram import Client
from pyrogram.types import CallbackQuery

from SmartConverter.Plugins.converter import *
from SmartConverter.translation import Translation

@TGBot.on_message(filters.command("start", prefixes=["/", "."]))
async def start_cmd_handler(bot, message):
  await message.reply_video(
    video="https://telegra.ph/file/d344fcd1367121197eccc.mp4",
    caption=Translation.START_TEXT,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙷𝙴𝙻𝙿✫", url="https://t.me/TG_FileConverterBot?start=help"),
          InlineKeyboardButton("✫𝙰𝙱𝙾𝚄𝚃✫", url="https://t.me/TG_FileConverterBot?start=about")
        ],
        [
          InlineKeyboardButton("✫𝙽𝙴𝚃𝚆𝙾𝚁𝙺✫", url="http://t.me/StrawHat_Network")
        ],
      ],
    ),
    parse_mode="md",
    quote=True
  )


@TGBot.on_message(filters.command("help", prefixes=["/", "."]))
async def help_message(bot, message):
  await message.reply_video(
    video="https://telegra.ph/file/ebd8a53dafca84ac0f8ff.mp4",
    caption=Translation.HELP_TEXT,
    parse_mode="markdown"
  )
  



@TGBot.on_message(filters.command("about", prefixes=["/", "."]))
async def about_message(bot, message):
  await message.reply_video(
    video="https://telegra.ph/file/33186a24917037de0d97a.mp4",
    caption=Translation.ABOUT_TEXT,
    parse_mode="markdown"
  )