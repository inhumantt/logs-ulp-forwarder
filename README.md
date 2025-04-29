# logs-ulp-forwarder
this script can be used to forward logs files or ulp files from public channel/group to your channel/group

This is a Python script using [Telethon](https://github.com/LonamiWebs/Telethon) that listens to new messages in one or more Telegram channels and automatically forwards media files (photos, documents like `.zip`, `.rar`, etc.) to a specified destination chat.

## Features

- Forwards only media messages (photo/document).
- Skips duplicates (prevents re-forwarding the same file).
- Adds a delay before forwarding to avoid rate limits.
- Works with multiple source channels.

## Requirements

- Python 3.7+
- A Telegram account (this uses your user account, **not** a bot token).
- Telethon

## Installation

1. **Clone the repo**:

    ```bash
    git clone https://github.com/yourusername/telegram-file-forwarder.git
    cd telegram-file-forwarder
    ```

2. **Install dependencies**:

    ```bash
    pip install telethon
    ```

3. **Run the script**:

    ```bash
    python forward_files.py
    ```

    You'll be prompted to enter:

    - Your Telegram **API ID** and **API Hash**  
      Get these from [https://my.telegram.org](https://my.telegram.org).
    - One or more **source channel IDs** (comma-separated).
    - A **destination chat ID**.

## Notes

- The first time you run the script, Telethon will ask for your phone number and verification code to log in.
- This script uses a local session (`user_session.session`) to stay logged in.
- You must be a member of the source channels and have permission to forward from them.

## License

MIT License
