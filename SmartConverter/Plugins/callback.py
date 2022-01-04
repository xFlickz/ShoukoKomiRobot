from SmartConverter.Plugins.ebook_converter import *

from SmartConverter.Plugins.pdf import p_d_f

@TGBot.on_callback_query()
async def pdf_call(bot ,m):
  if m.data == "pdf":
    await p_d_f(
      file_name, 
      o, 
      m
    )
    logger.info(o)
    if o is not None:
      await m.edit_text("Uploading")
      await bot.send_document(
        chat_id=m.chat.id,
        document=o,
        force_document=True,
        caption="Here is your pdf",
       # reply_to_message_id=m.message_id,
        progress=progress_for_pyrogram,
        progress_args=(bot, "Uploading", m, c_time
        )
      )
      os.remove(o)
      await bot.edit_message_text(
        chat_id=m.chat.id,
        text="Uploaded below..",
        disable_web_page_preview=True,
        message_id=m.message_id
      )