"""
This Bot Was Developed By The Owner Of @XFlick.
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
          InlineKeyboardButton("✫𝙳𝙴𝚅✫", url="https://t.me/XFlick"),
          InlineKeyboardButton("✫Group✫", url="https://t.me/+hpCwlBcPJtI1ZDU9")
        ],

        [
          InlineKeyboardButton("✫𝙷𝙴𝙻𝙿✫", callback_data="hilp")
        ],
      ],
    ),
    parse_mode="md"
  )



async def help_message(bot, update):
  await update.message.edit_caption(
    caption=Translation.HELP_TEXT,
    parse_mode="markdown",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙷𝙾𝙼𝙴✫", callback_data="beck")
        ],
      ],
    )
  )

@TGBot.on_message(filters.command("help", prefixes=["/", "."]))
async def help_single_message(bot, message):
  await message.reply_video(
    video="https://telegra.ph/file/ebd8a53dafca84ac0f8ff.mp4",
    caption=Translation.HELP_TEXT,
    parse_mode="markdown",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙽𝙴𝚃𝚆𝙾𝚁𝙺✫", url="https://t.me/AnimeXflickz")
        ],
      ],
    )
  )



async def back_handler(bot, update):
  await update.message.edit_caption(
    caption=Translation.START_TEXT,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙳𝙴𝚅✫", url="https://t.me/XFlick"),
          InlineKeyboardButton("✫𝙽𝙴𝚃𝚆𝙾𝚁𝙺✫", url="https://t.me/AnimeXflickz")
        ],
        [
          InlineKeyboardButton("✫𝙷𝙴𝙻𝙿✫", callback_data="hilp")
        ],
      ],
    ),
    parse_mode="md"
  )
# Restart and eval in next update 
