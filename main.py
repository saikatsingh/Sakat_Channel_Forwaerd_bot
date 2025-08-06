from pyrogram import Client, filters
from pyrogram.session import StringSession
import os

# 📦 Env variables (set in Koyeb)
API_ID = int(os.getenv("USERBOT_API_ID", "20389440"))
API_HASH = os.getenv("USERBOT_API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID", "-1001234567890"))
DEST_CHANNEL_ID = int(os.getenv("DEST_CHANNEL_ID", "-1009876543210"))

# 🔐 Your actual string session here
STRING_SESSION = "📌 paste your full string session here"

# 🤖 Start userbot with StringSession
app = Client(
    name=StringSession(STRING_SESSION),
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True
)

# 🔁 Forward messages from source to destination
@app.on_message(filters.chat(SOURCE_CHANNEL_ID))
async def forward_to_dest(client, message):
    try:
        await message.copy(DEST_CHANNEL_ID)
        print(f"✅ Forwarded: {message.text or message.caption}")
    except Exception as e:
        print(f"⚠️ Failed to forward: {e}")

# 🚀 Start the app
app.run()
