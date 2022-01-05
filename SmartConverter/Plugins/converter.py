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
import asyncio
from .. import TGBot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@TGBot.on_message(filters.incoming & (filters.video | filters.document))
async def pdf_message(bot, message):
  if message.chat.id not in Config.AUTH_USERS:
    await message.reply_text("🚷 No Outsider Allowed ⚠️\n\nThis Bot is For Private Use Only.")
    return
  
  await message.reply_text(
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
          InlineKeyboardButton("Txt", callback_data="txt")],
      ],
    ),
    quote=True,
    parse_mode="markdown"
  )
# ---------------------------------------

# if clicked pdf

@TGBot.on_callback_query()
async def pdf_call(bot ,update):
  if update.data == "pdf":
    await update.message.delete()
    
    download_location = Config.DOWNLOAD_LOCATION + "/"
    #bot_msg = await bot.get_messages(update.message.chat.id, update.message.reply_to_message.message_id
    await asyncio.sleep(1)
    #todown = bot_msg.reply_to_message
    sent_message = await bot.send_message(
      text="`Downloading ...`",
      chat_id=update.message.chat.id,
      reply_to_message_id=update.message.reply_to_message.message_id
    )
    c_time = time.time()
    f_n = await bot.download_media(
      message=update.message.reply_to_message,
      file_name=download_location,
      progress=progress_for_pyrogram,
      progress_args=(
        bot,
        "`Downloading ...`",
        sent_message,
        c_time
      )
    )
    logger.info(f_n)
    
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Video Format not Allowed!",
        message_id=sent_message.message_id
      )
        #message_id=sent_message.message_id
    # rename file as .pdf and convert using ebook convert 
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".pdf")
    if f_n is not None:
      await bot.edit_message_text(
        text="`Processing your file ... 👀`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`Converting Your File In Pdf Format ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      subprocess.run(
        ["ebook-convert", f_n, o],
        env={"QTWEBENGINE_CHROMIUM_FLAGS": "--no-sandbox"},
      )
    logger.info(o)
    if o is not None:
      await bot.edit_message_text(
        text="`Uploading ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
       # reply_to_message_id=m.message_id,
        progress=progress_for_pyrogram,
        progress_args=(bot, "`Uploading ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "epub":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`Downloading ...`",
      chat_id=update.message.chat.id,
      reply_to_message_id=update.message.reply_to_message.message_id
    )
    c_time = time.time()
    f_n = await bot.download_media(
      message=update.message.reply_to_message,
      file_name=download_location,
      progress=progress_for_pyrogram,
      progress_args=(
        bot,
        "`Downloading ...`",
        sent_message,
        c_time
      )
    )
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Video Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".epub")
    if f_n is not None:
      await bot.edit_message_text(
        text="`Processing your file ... 👀`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`Converting Your File In Epub Format ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      subprocess.run(
        ["ebook-convert", f_n, o],
        env={"QTWEBENGINE_CHROMIUM_FLAGS": "--no-sandbox"},
      )
    logger.info(o)
    if o is not None:
      await bot.edit_message_text(
        text="`Uploading ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
         # reply_to_message_id=m.message_id,
        progress=progress_for_pyrogram,
        progress_args=(bot, "`Uploading ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "cbz":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`Downloading ...`",
      chat_id=update.message.chat.id,
      reply_to_message_id=update.message.reply_to_message.message_id
    )
    c_time = time.time()
    f_n = await bot.download_media(
      message=update.message.reply_to_message,
      file_name=download_location,
      progress=progress_for_pyrogram,
      progress_args=(
        bot,
        "`Downloading ...`",
        sent_message,
        c_time
      )
    )
  
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Video Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".cbz")
    if f_n is not None:
      await bot.edit_message_text(
        text="`Processing your file ... 👀`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`Converting Your File In Cbz Format ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      subprocess.run(
        ["ebook-convert", f_n, o],
        env={"QTWEBENGINE_CHROMIUM_FLAGS": "--no-sandbox"},
      )
    logger.info(o)
    if o is not None:
      await bot.edit_message_text(
        text="`Uploading ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
        progress=progress_for_pyrogram,
        progress_args=(bot, "`Uploading ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
      