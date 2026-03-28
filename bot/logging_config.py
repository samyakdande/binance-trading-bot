import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    force=True   # 🔥 IMPORTANT
)

logger = logging.getLogger(__name__)