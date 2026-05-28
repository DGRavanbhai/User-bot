# Telegram Userbot

A cleaned-up Telethon-based multi-client userbot starter.

## Features
- Ping command
- Reboot command
- Owner-only sudo add command
- Up to 10 session strings

## Project files
- `main.py` — app entry point
- `clients.py` — creates Telethon clients
- `handlers/admin.py` — admin commands
- `config.py` — environment configuration
- `utils/` — helper and storage utilities

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file:
```env
API_ID=12345
API_HASH=your_api_hash
OWNER_ID=123456789
CMD_HNDLR=.
SESSION_1=your_string_session_here
# Optional
SESSION_2=
SESSION_3=
SESSION_4=
SESSION_5=
SESSION_6=
SESSION_7=
SESSION_8=
SESSION_9=
SESSION_10=
```

3. Run the bot:
```bash
python main.py
```

## Notes
- Do not commit `.env` or session strings to GitHub.
- If you use Heroku, set `HEROKU_API_KEY` and `HEROKU_APP_NAME`.
- Local sudo users are stored in `data/sudo_users.json`.
