from bot.logging_config import logger   # MUST be first
import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import logger


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot (Testnet)"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        # --- LOG INPUT ---
        logger.info(
            f"CLI Input | symbol={args.symbol} | side={args.side} | type={args.type} | qty={args.quantity} | price={args.price}"
        )

        # --- VALIDATE ---
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        # --- EXECUTE ORDER ---
        if args.type == "MARKET":
            result = place_market_order(
                args.symbol, args.side, args.quantity
            )
        else:
            result = place_limit_order(
                args.symbol, args.side, args.quantity, args.price
            )

        # --- PRINT OUTPUT ---
        print("\n✅ Order Placed Successfully")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        print("\n📊 Response:")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Executed Qty: {result.get('executedQty', 'N/A')}")
        print(f"Avg Price: {result.get('avgPrice', 'N/A')}")

        # --- LOG SUCCESS ---
        logger.info(
            f"CLI Success | ID={result['orderId']} | Status={result['status']} | ExecutedQty={result.get('executedQty')}"
        )

    except Exception as e:
        # --- LOG ERROR ---
        logger.error(f"CLI Error | {str(e)}")

        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main(logger.info("🚀 CLI started"))