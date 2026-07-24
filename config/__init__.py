"""
Centralized configuration for the VC-to-VC forwarding userbot.

All environment variables are read exactly once, validated, and exposed
as typed module-level constants so every other module can simply do
`import config` and use `config.API_ID`, etc.
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()


def _require(name: str) -> str:
    value = os.environ.get(name)
    if value is None or value.strip() == "":
        sys.exit(f"[config] Missing required environment variable: {name}")
    return value.strip()


def _require_int(name: str) -> int:
    raw = _require(name)
    try:
        return int(raw)
    except ValueError:
        sys.exit(f"[config] Environment variable {name} must be an integer, got: {raw!r}")


# ---- Telegram credentials -------------------------------------------------
API_ID: int = _require_int("API_ID")
API_HASH: str = _require("XFJ4YR4NMZF7Y3IMLGU7QXC3MNNQ3MLT")
BOT_TOKEN: str = _require("8819187387:AAFWOiarYyJgSRwZv5GHvpT_k8LWLdmx30s")
STRING_SESSION: str = _require("BQHBWlEAmCSIVsmv0EGRpYFdhxFW-t4b_TJ35QeSmioDVA_7noAPHRnRcNGG4ckO9rKsaJGQbKkEK83aea784UMvqDOme8GtCX2GeZztWdWJFWyjVWfatnmwcBJ9W-w1nTcAxFndR9D35lLwtKyZajpn7J_LaJGvfqZ1f9yCuBOHjObgt3FZesMyZtAljXfvvIINUeNu8VMoAa-yAJS6DZGSG3k9S80Uv6blFiGtmkr54QjbdDvejRsClstYXtSPNiNkDmcyqrAgouQb6VkUui6WtLS63vWO0pF-yNc59FcI7Ke40rZGyUo_UOkLhQI3lTuteaMBiKr6zO4jJblrXt07D69IsAAAAAH9eT-jAA")
OWNER_ID: int = _require_int("8417510906")

# ---- Group configuration ---------------------------------------------------
RECORD_GROUP: int = _require_int("-1002389305159")
LOGGER_GROUP: int = _require_int("-1003799579979")

# ---- Database ---------------------------------------------------------------
MONGO_URI: str = _require("mongodb+srv://Sweettoxic:Sweettoxic@sweettoxic.mg57v4c.mongodb.net/?retryWrites=true&w=majority")
DB_NAME: str = _require("telegrambot")

# ---- Audio bridge -------------------------------------------------------
PULSE_SINK_NAME: str = os.environ.get("PULSE_SINK_NAME", "vcrelay").strip() or "vcrelay"

# ---- Filesystem -------------------------------------------------------------
WORK_DIR: str = os.environ.get("WORK_DIR", "/tmp/vc_forward_bot").strip() or "/tmp/vc_forward_bot"
LOG_DIR: str = os.path.join(WORK_DIR, "logs")
PIPE_DIR: str = os.path.join(WORK_DIR, "pipes")
RECORDINGS_DIR: str = os.path.join(WORK_DIR, "recordings")
SCREEN_SHARE_DEVICE: str = os.environ.get("SCREEN_SHARE_DEVICE", ":1.0")

for _directory in (WORK_DIR, LOG_DIR, PIPE_DIR, RECORDINGS_DIR):
    os.makedirs(_directory, exist_ok=True)

# ---- Audio defaults -----------------------------------------------------
DEFAULT_LEVEL: int = 5   # 1-25
DEFAULT_BASS: int = 0    # 0-15
MIN_LEVEL, MAX_LEVEL = 1, 25
MIN_BASS, MAX_BASS = 0, 15

SESSION_NAME_ASSISTANT = "assistant_session"
SESSION_NAME_BOT = "bot_session"
