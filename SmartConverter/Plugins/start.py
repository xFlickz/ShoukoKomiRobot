"""
This Bot Was Developed By The Owner Of @StrawHat_Network.
Join his network and support him.
"""

from SmartConverter.Plugins.converter import *
from SmartConverter.translation import Translation

@TGBot.on_message(filters.command("start", prefixes=["/", "."]))
async def start_cmd_handler(bot, message):
  await message.reply_video(
    video="https://telegra.ph/file/f7006e236e28ba090d407.mp4",
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
    parse_mode="markdown",
    quote=True
  )
  
@TGBot.on_callback_query()
async def helpo(bot, message):
  data = message.data 
  if data == "help":
    await message.message.delete()
    #await message.message.edit_text(
      #text=Translation.HELP_TEXT,
      #parse_mode="markdown",
      #reply_markup=InlineKeyboardMarkup(
        #[
          #[InlineKeyboardButton("✫𝙱𝙰𝙲𝙺✫", callback_data="back")],
        #],
      #)
    #)
  elif data == "about":
    await message.message.edit_text(
      caption="**LANGUAGE** [Python](https://www.python.org)\n**LIBRARY** [Pyrogram](https://www.pyrogram.org)\n**SOURCE CODE** [Click me](https://t.me/Shity_man)\n**DEV** [Dark](https://t.me/Bro_isDarkal)",
      disable_web_page_preview=True,
      parse_mode="markdown",
      reply_markup=InlineKeyboardMarkup(
        [
          [InlineKeyboardButton("✫𝙱𝙰𝙲𝙺✫", callback_data="back")],
        ],
      )
    )
  elif data == "back":
    await message.message.edit_media(
      media="https://telegra.ph/file/f7006e236e28ba090d407.mp4",
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