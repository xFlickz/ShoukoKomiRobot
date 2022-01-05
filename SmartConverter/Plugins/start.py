# (c) Dark
from SmartConverter.Plugins.converter import *

@TGBot.on_message(filters.command("start", prefixes=["/", "."]))
async def start_cmd_handler(bot, message):
  await bot.send_video(
    chat_id=message.chat.id,
    video="BAADBAADIgsAAjyBsVKGb3ptgjvluQI",
    caption="**Hello** {message.from_user.mention}\nI am Telegram SmartConverter Bot that converts files' format in your desired one.\nMy owner will reveal the open source soon. Support me by joining my network and channel 😇.",
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
    await bot.send_message(
      chat_id=m.message.chat.id,
      text="• Send me a file.\n• Click the desired format button.\n• Bot will download , convert and upload.",
      parse_mode="markdown"
    )
  elif m.data == "about":
    await m.message.delete()
    await bot.send_message(
      chat_id=m.message.chat.id,
      text="**LANGUAGE** [Python](https://www.python.org)\n**LIBRARY** [Pyrogram](https://www.pyrogram.org)\n**SOURCE CODE** [Click me](https://t.me/Shity_man)",
      parse_mode="markdown"
    )
      
      
    
        