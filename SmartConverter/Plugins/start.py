# (c) Dark
from SmartConverter.Plugins.converter import *
from translation import Translation

@TGBot.on_message(filters.command("start", prefixes=["/", "."]))
async def start_cmd_handler(bot, message):
  await bot.send_video(
    chat_id=message.chat.id,
    video="https://telegra.ph/file/f7006e236e28ba090d407.mp4",
    caption=Translation.START_TEXT,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("Help", callback_data="help"),
          InlineKeyboardButton("About", callback_data="about")
        ],
        [
          InlineKeyboardButton("Network", url="http://t.me/StrawHat_Network")
        ],
      ],
    ),
    parse_mode="markdown"
  )
  
@TGBot.on_callback_query()
async def helpo(bot, m):
  if m.data == "help":
    await m.message.delete()
    await bot.send_video(
      chat_id=m.message.chat.id,
      video="https://telegra.ph/file/33186a24917037de0d97a.mp4",
      text=Translation.HELP_TEXT,
      parse_mode="markdown",
      reply_markup=InlineKeyboardMarkup(
        [
          [InlineKeyboardButton("Back", callback_data="back")],
        ],
      )
    )
  elif m.data == "about":
    await m.message.delete()
    await bot.send_video(
      chat_id=m.message.chat.id,
      video="https://telegra.ph/file/a7f47db6297329258755e.mp4",
      caption="**LANGUAGE** [Python](https://www.python.org)\n**LIBRARY** [Pyrogram](https://www.pyrogram.org)\n**SOURCE CODE** [Click me](https://t.me/Shity_man)\n**DEV** [Dark](https://t.me/Bro_isDarkal)",
      parse_mode="markdown",
      reply_markup=InlineKeyboardMarkup(
        [
          [InlineKeyboardButton("Back", callback_data="back")],
        ],
      )
    )
  elif m.data == "back":
    await m.message.delete()
    await bot.send_video(
      chat_id=m.message.chat.id,
      video="https://telegra.ph/file/f7006e236e28ba090d407.mp4",
      caption=Translation.START_TEXT,
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
          ],
          [
            InlineKeyboardButton("Network", url="http://t.me/StrawHat_Network")
          ],
        ],
      ),
      parse_mode="markdown"
    )