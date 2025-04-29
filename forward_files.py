import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

# Get user input for API credentials and channel IDs
api_id = int(input("Enter your API ID: "))
api_hash = input("Enter your API Hash: ")

# Ask for source channels (comma-separated)
source_channels_input = input("Enter source channel IDs (comma-separated): ")
source_channels = [int(x.strip()) for x in source_channels_input.split(",")]

# Ask for destination chat
destination_chat = int(input("Enter the destination chat ID: "))

# Initialize client
client = TelegramClient("user_session", api_id, api_hash)

# Set to keep track of already forwarded file IDs
forwarded_files = set()

@client.on(events.NewMessage(chats=source_channels))
async def forward_files(event):
    if event.message.media:
        file_id = None

        if isinstance(event.message.media, MessageMediaPhoto):
            file_id = event.message.media.photo.id
        elif isinstance(event.message.media, MessageMediaDocument):
            file_id = event.message.media.document.id

        if file_id and file_id not in forwarded_files:
            forwarded_files.add(file_id)
            await asyncio.sleep(2)
            await event.message.forward_to(destination_chat)
            print(f"Forwarded file {file_id} from channel {event.chat_id}")

# Start the client
client.start()
print("Listening for new files with delay...")
client.run_until_disconnected()
