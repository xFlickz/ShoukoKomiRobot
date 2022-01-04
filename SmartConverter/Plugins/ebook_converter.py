import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
import shutil
import time
from config import Config 
from SmartConverter.Tools.progress import ( TimeFormatter,
  progress_for_pyrogram
)
import subprocess
from .. import TGBot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@TGBot.on_message(filters.incoming & (filters.video | filters.document))
async def pdf_message(bot, update):
    return await update.reply_text("🚷 No Outsider Allowed ⚠️\n\nThis Bot is For Private Use Only.")
  download_location = Config.DOWNLOAD_LOCATION + "/"
  sent_message = await bot.send_message(
    chat_id=update.chat.id,
    text="Downloading",
    reply_to_message_id=update.message_id
  )
  c_time = time.time()
  file_name = await bot.download_media(
    message=update,
    #file_name=download_location,
    progress=progress_for_pyrogram,
    progress_args=(
      bot,
      "Downloading",
      sent_message,
      c_time
    )
  )
  logger.info(file_name)
  
  if file_name.rsplit(".", 1)[-1].lower() not in ["epub", "pdf", "cbz", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
    return await bot.edit_message_text(
      chat_id=update.chat.id,
      text="This Video Format not Allowed!",
      message_id=sent_message.message_id
    )
    
  await bot.edit_message_text(
    chat_id=update.chat.id,
    text="Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ Yᴏᴜ Wᴀɴɴᴀ Cᴏɴᴠᴇʀᴛ",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("Pdf", callback_data="pdf"),
          InlineKeyboardButton("Epub", callback_data="epub"),
          InlineKeyboardButton("Cbz", callback_data="cbz")
        ],
        [
          InlineKeyboardButton("Docx",callback_data="docx"),
          InlineKeyboardButton("Doc", callback_data="doc"),
          InlineKeyboardButton("Txt", callback_data="txt")
        ],
      ],
    ),
    message_id=sent_message.reply_to_message_id
  )
  

    
        
  