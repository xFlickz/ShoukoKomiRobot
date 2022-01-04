import asyncio
import logging
from os import path
from config import Config
from pyrogram import (
  Client, 
  idle
)


class TGclient(Client):
  def __init__(self):
    super().__init__(
      "TGclient",
      api_id=Config.API_ID,
      api_hash=Config.API_HASH,
      bot_token=Config.BOT_TOKEN,
      workdir="./",
      plugins=dict(root="SmartConverter/Plugins")
    )
    bot_info = None
  
  async def __run(self):
    await super().start()
    self.bot_info  = await self.get_me()
    logging.info(f"@{self.bot_info.username} has started")
    await idle()
    
  def run(self):
    asyncio.get_event_loop().run_until_complete(self.__run())