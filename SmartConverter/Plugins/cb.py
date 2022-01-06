from SmartConverter.Plugins.converter import *
from SmartConverter.Plugins.helper import *

async def help_message(bot, update):
  await update.message.delete()
  await asyncio.sleep(0.5)
  await bot.send_video(
    chat_id=update.message.chat.id,
    video="https://telegra.ph/file/ebd8a53dafca84ac0f8ff.mp4",
    caption=Translation.HELP_TEXT,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙷𝙾𝙼𝙴✫", callback_data="home")
        ],
      ],
    ),
    parse_mode="markdown"
  )

async def about_message(bot, update):
  await bot.messages.delete(chat_id=update.message.chat.id, message_ids=update.message.message_id)
  await bot.send_video(
    chat_id=update.message.chat.id,
    video="https://telegra.ph/file/33186a24917037de0d97a.mp4",
    caption=Translation.ABOUT_TEXT,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙰𝙱𝙾𝚄𝚃✫", callback_data="about")
        ],
      ],
    ),
    parse_mode="markdown"
  )
  

async def back_message(bot, update):
  await bot.messages.delete(chat_id=update.message.chat.id, message_ids=update.message.message_id)
  await bot.send_video(
    chat_id=update.message.chat.id,
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
    parse_mode="markdown"
  )