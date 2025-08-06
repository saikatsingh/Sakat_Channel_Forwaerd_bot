import os
from pyrogram import Client, filters
from pyrogram.session.string_session import StringSession

# Get environment variables
API_ID = int(os.environ.get("USERBOT_API_ID"))
API_HASH = os.environ.get("USERBOT_API_HASH")
SESSION_STRING = os.environ.get("USER_SESSION_STRING")
SOURCE_CHANNEL_ID = int(os.environ.get("SOURCE_CHANNEL_ID"))
DEST_CHANNEL_ID = int(os.environ.get("DEST_CHANNEL_ID"))

# Create userbot client
app = Client(
    session_name=StringSession(SESSION_STRING),
    api_id=API_ID,
    api_hash=API_HASH
)

# Forward messages from source to destination
@app.on_message(filters.chat(SOURCE_CHANNEL_ID))
async def forward_message(client, message):
    try:
        await message.copy(DEST_CHANNEL_ID)
        print("✅ Message forwarded")
    except Exception as e:
        print(f"❌ Error: {e}")

app.run()
