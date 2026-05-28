import os
from dotenv import load_dotenv

load_dotenv()

def _required_int(name: str) -> int:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    if not value.isdigit():
        raise RuntimeError(f"{name} must be a numeric Telegram ID")
    return int(value)

API_ID = _required_int("API_ID")
API_HASH = os.getenv("API_HASH", "").strip()
if not API_HASH:
    raise RuntimeError("Missing required environment variable: API_HASH")

OWNER_ID = _required_int("OWNER_ID")
CMD_HNDLR = os.getenv("CMD_HNDLR", ".").strip() or "."

SUDO_USERS = {OWNER_ID}
for part in os.getenv("SUDO_USERS", "").replace(",", " ").split():
    if part.isdigit():
        SUDO_USERS.add(int(part))
