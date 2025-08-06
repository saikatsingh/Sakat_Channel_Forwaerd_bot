from os import getenv
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# ----------------------- CONFIG -----------------------
class Config:
    # Bot credentials
    API_ID = int(getenv("API_ID", "123456"))
    API_HASH = getenv("API_HASH", "your_default_hash")
    BOT_TOKEN = getenv("BOT_TOKEN", "your_default_token")
    
    # Bot forward channels
    CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001234567890:-1009876543210").replace("\n", " ").split(":"))

    # Userbot credentials
    USERBOT_API_ID = int(getenv("USERBOT_API_ID", API_ID))
    USERBOT_API_HASH = getenv("USERBOT_API_HASH", API_HASH)
    SOURCE_CHANNEL_ID = int(getenv("SOURCE_CHANNEL_ID", "-1001122334455"))
    DEST_CHANNEL_ID = int(getenv("DEST_CHANNEL_ID", "-1009988776655"))

# --------------------- BOT CLIENT ---------------------
bot = Client(
    "forwarder-bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Forwarding via bot (only works if bot is admin)
@bot.on_message(filters.channel & filters.incoming)
async def bot_forward(client: Client, message: Message):
    for dest in Config.CHANNEL:
        try:
            await message.forward(dest)
        except Exception as e:
            print(f"[BOT ERROR] {e}")

# ------------------ USERBOT CLIENT --------------------
userbot = Client(
    "userbot",
    api_id=Config.USERBOT_API_ID,
    api_hash=Config.USERBOT_API_HASH,
    in_memory=True
)

# Forwarding as user (from source channel to destination)
@userbot.on_message(filters.chat(Config.SOURCE_CHANNEL_ID) & filters.channel)
async def userbot_forward(client: Client, message: Message):
    try:
        await message.forward(Config.DEST_CHANNEL_ID)
    except Exception as e:
        print(f"[USERBOT ERROR] {e}")

# -------------------- RUN BOTH ------------------------
async def main():
    await userbot.start()
    await bot.start()
    print("Both bot and userbot are running.")
    await idle()

from pyrogram import idle

if __name__ == '__main__':
    asyncio.run(main())
