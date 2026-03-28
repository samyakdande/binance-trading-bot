import time
from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"Placing MARKET order | {symbol} | {side} | qty={quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        order_id = order['orderId']

        # Wait for execution update
        time.sleep(1)

        updated_order = client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        logger.info(
            f"Order Success | ID={order_id} | Status={updated_order['status']} | ExecutedQty={updated_order['executedQty']}"
        )

        return updated_order

    except Exception as e:
        logger.error(f"MARKET Order Failed | Error={str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"Placing LIMIT order | {symbol} | {side} | qty={quantity} | price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=str(price),
            timeInForce="GTC"
        )

        logger.info(
            f"Limit Order Placed | ID={order['orderId']} | Status={order['status']}"
        )

        return order

    except Exception as e:
        logger.error(f"LIMIT Order Failed | Error={str(e)}")
        raise