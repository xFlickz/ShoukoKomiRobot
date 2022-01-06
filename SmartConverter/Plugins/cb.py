from SmartConverter.Plugins.converter import *

@TGBot.on_callback_query()
async def pdf_call(bot ,update):
  if update.data == "pdf":
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
    if f_n.rsplit(".", 1)[-1].lower() not in ["epub", "cbz", "pdf", "docx", "doc", "ppt", "mobi", "txt", "zip"]:
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
  