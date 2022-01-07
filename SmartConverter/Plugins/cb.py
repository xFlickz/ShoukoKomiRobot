from SmartConverter.Plugins.converter import *
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
@TGBot.on_callback_query()
async def calls(bot ,update):
  if update.data == "video_file":
    await update.message.edit_text(
      text="Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ Yᴏᴜ Wᴀɴɴᴀ Cᴏɴᴠᴇʀᴛ",
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("✫𝙼𝙿4✫", callback_data="mp4"),
            InlineKeyboardButton("✫𝙼𝙺𝚅✫", callback_data="mkv"),
            InlineKeyboardButton("✫𝚂𝚃𝚁𝙴𝙰𝙼✫", callback_data="stream")
          ],
          [
            InlineKeyboardButton("🔙", callback_data="back_to")],
        ],
      )
    )
    
  elif update.data == "back_to":
    await update.message.delete()
    await update.message.reply_text(
      text="Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ Yᴏᴜ Wᴀɴɴᴀ Cᴏɴᴠᴇʀᴛ",
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("✫𝙿𝙳𝙵✫", callback_data="pdf"),
            InlineKeyboardButton("✫𝙴𝙿𝚄𝙱✫", callback_data="epub"),
            InlineKeyboardButton("✫𝙲𝙱𝚉✫", callback_data="cbz")
          ],
          [
            InlineKeyboardButton("✫𝙳𝙾𝙲𝚇✫",callback_data="docx"),
            InlineKeyboardButton("✫𝙷𝚃𝙼𝙻✫", callback_data="doc"),
            InlineKeyboardButton("✫𝚃𝚇𝚃✫", callback_data="txt")
          ],
          [
            InlineKeyboardButton("✫𝚅𝙸𝙳𝙴𝙾 𝚄𝚃𝙸𝙻𝚂✫", callback_data="video_file")],
        ],
      ),
      quote=True,
      parse_mode="markdown"
    )
  elif update.data == "pdf":
    await update.message.delete()
    
    download_location = Config.DOWNLOAD_LOCATION + "/"
    #bot_msg = await bot.get_messages(update.message.chat.id, update.message.reply_to_message.message_id
    await asyncio.sleep(1)
    #todown = bot_msg.reply_to_message
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
    logger.info(f_n)
    
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
        #message_id=sent_message.message_id
    # rename file as .pdf and convert using ebook convert 
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".pdf")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
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
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
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
        progress_args=(bot, "`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "hilp":
    await help_message(bot, update)
  elif update.data == "beck":
    await back_handler(bot, update)
  elif update.data == "epub":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".epub")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
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
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
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
        progress_args=(bot, "`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "cbz":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
  
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".cbz")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
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
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
        progress=progress_for_pyrogram,
        progress_args=(bot, "`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "docx":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
    
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".docx")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
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
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
        progress=progress_for_pyrogram,
        progress_args=(bot, "`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "doc":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
      
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".html")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
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
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
        progress=progress_for_pyrogram,
        progress_args=(bot, "`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "txt":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
        
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".txt")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
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
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
        progress=progress_for_pyrogram,
        progress_args=(bot,"`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  # video utils ( mp4 , mkv , stream)
  elif update.data == "mp4":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
          
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["mkv", "mp4", "webm"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
        )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".mp4")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      os.rename(f_n, o)
      
    logger.info(o)
    if o is not None:
      await bot.edit_message_text(
        text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await bot.send_document(
        chat_id=update.message.chat.id,
        document=o,
        force_document=True,
        caption=f"**{o}**",
        progress=progress_for_pyrogram,
        progress_args=(bot,"`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
        )
      )
      os.remove(o)
      await sent_message.delete()
  elif update.data == "mkv":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
            
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["mkv", "mp4", "webm"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", ".mkv")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      os.rename(f_n, o)
        
      logger.info(o)
      if o is not None:
        await bot.edit_message_text(
          text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
          chat_id=update.message.chat.id,
          message_id=sent_message.message_id
        )
        await bot.send_document(
          chat_id=update.message.chat.id,
          document=o,
          force_document=True,
          caption=f"**{o}**",
          progress=progress_for_pyrogram,
          progress_args=(bot,"`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
          )
        )
        os.remove(o)
        await sent_message.delete()
  elif update.data == "stream":
    await update.message.delete()
    download_location = Config.DOWNLOAD_LOCATION + "/"
    await asyncio.sleep(1)
    sent_message = await bot.send_message(
      text="`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
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
        "`𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 ...`",
        sent_message,
        c_time
      )
    )
              
    logger.info(f_n)
    if f_n.rsplit(".", 1)[-1].lower() not in ["mkv", "mp4", "webm"]:
      return await bot.edit_message_text(
        chat_id=update.message.chat.id,
        text="This Format not Allowed!",
        message_id=sent_message.message_id
      )
    kk = f_n.split("/")[-1]
    aa = kk.split(".")[-1]
    o = kk.replace(f".{aa}", "Stream.mp4")
    if f_n is not None:
      await bot.edit_message_text(
        text="`𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      await asyncio.sleep(1)
      await bot.edit_message_text(
        text="`𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚒𝚗𝚐 ...`",
        chat_id=update.message.chat.id,
        message_id=sent_message.message_id
      )
      os.rename(f_n, o)
      
      width = 0
      height = 0
      duration = 0
      metadata = extractMetadata(createParser(o))
      if metadata.has("duration"):
        duration = metadata.get('duration').seconds
      if metadata.has("width"):
        width = metadata.get("width")
      if metadata.has("height"):
        height = metadata.get("height")
        
      logger.info(o)
      if o is not None:
        await bot.edit_message_text(
          text="`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`",
          chat_id=update.message.chat.id,
          message_id=sent_message.message_id
        )
        await bot.send_video(
          chat_id=update.message.chat.id,
          video=o,
          duration=duration,
          width=width,
          height=height,
          supports_streaming=True,
          caption=f"**{o}**",
          progress=progress_for_pyrogram,
          progress_args=(bot,"`𝚄𝚙𝚕𝚊𝚘𝚍𝚒𝚗𝚐 ...`", sent_message, c_time
          )
        )
        os.remove(o)
        await sent_message.delete()
        
        
# (c) DARK