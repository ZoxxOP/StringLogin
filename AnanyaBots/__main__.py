import asyncio
import importlib

from pyrogram import idle
from AnanyaBots import LOG
from AnanyaBots.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("AnanyaBots.modules." + all_module)
    LOG.print("[bold yellow]ʜᴀᴄᴋ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ɴᴏᴡ ғᴜᴄᴋ ᴀʟʟ ᴛɢ ɪᴅ")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄʟᴇ ᴀʟʟ ᴛᴀsᴛ🤐..........")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
