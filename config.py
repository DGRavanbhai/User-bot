from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Set

from dotenv import load_dotenv

load_dotenv()


def _int_env(name: str, default: int = 0) -> int:
    value = os.getenv(name, str(default)).strip()
    try:
        return int(value)
    except ValueError:
        return default


def _split_ints(raw: str) -> Set[int]:
    result: Set[int] = set()
    for chunk in raw.split():
        try:
            result.add(int(chunk))
        except ValueError:
            continue
    return result


API_ID = _int_env("API_ID")
API_HASH = os.getenv("API_HASH", "").strip()

OWNER_ID = _int_env("OWNER_ID")
CMD_HNDLR = os.getenv("CMD_HNDLR", ".").strip() or "."

HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "").strip()
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "").strip()

# Accept either space-separated SUDO_USER or SUDO_USERS.
SUDO_USERS = _split_ints(os.getenv("SUDO_USERS", "")) | _split_ints(os.getenv("SUDO_USER", ""))

# Support up to 10 session strings for multi-client usage.
SESSION_STRINGS: List[str] = [
    os.getenv(f"SESSION_{i}", "").strip()
    for i in range(1, 11)
]

# Backward-compatible aliases for the original project naming.
hl = CMD_HNDLR
