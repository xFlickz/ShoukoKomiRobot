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

async def p_d_f(dl, ul, message):
  kk = dl.split("/")[-1]
  aa = kk.split(".")[-1]
  ul = kk.replace(f".{aa}", ".pdf")
  if dl is not none:
    await message.edit_text("Converting In Pdf Format.")
    
    subprocess.run(
      ["ebook-convert", dl, ul],
      env={"QTWEBENGINE_CHROMIUM_FLAGS": "--no-sandbox"},
    )