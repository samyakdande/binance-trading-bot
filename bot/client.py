from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL
from bot.logging_config import logger


def get_client():
    try:
        client = Client(API_KEY, API_SECRET, testnet=True)
        client.FUTURES_URL = BASE_URL

        logger.info("Binance client initialized successfully")

        return client

    except Exception as e:
        logger.error(f"Failed to initialize client | Error={str(e)}")
        raise