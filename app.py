import streamlit as st
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.client import get_client
from bot.logging_config import logger
import time
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Trading Bot", layout="wide")

st.title("🚀 Binance Futures Trading Dashboard")

client = get_client()

# --- SESSION STATE FOR HISTORY ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- SYMBOLS ---
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]

# --- AUTO REFRESH ---
refresh_rate = st.sidebar.slider("🔄 Refresh Rate (sec)", 1, 10, 3)

# ================= LAYOUT =================
col1, col2 = st.columns(2)

# ================= LEFT =================
with col1:
    st.subheader("⚙️ Trade Settings")

    symbol = st.selectbox("Symbol", symbols)
    side = st.selectbox("Side", ["BUY", "SELL"])
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])

    quantity = st.number_input("Quantity", min_value=0.001, value=0.002)

    price = None
    if order_type == "LIMIT":
        price = st.number_input("Price", min_value=1.0, value=60000.0)

# ================= RIGHT =================
with col2:
    st.subheader("📊 Market Info")

    try:
        ticker = client.futures_symbol_ticker(symbol=symbol)
        live_price = float(ticker["price"])

        st.metric("Live Price", f"{live_price:.2f} USDT")

    except:
        live_price = None
        st.warning("Price unavailable")

    # --- VALIDATION ---
    if live_price:
        current_price = price if order_type == "LIMIT" else live_price
        notional = quantity * current_price

        st.metric("Order Value", f"{notional:.2f} USDT")

        if notional < 100:
            st.error("❌ Minimum 100 USDT")
        else:
            st.success("✅ Valid")

# ================= CHART =================
st.subheader("📈 Price Chart")

try:
    klines = client.futures_klines(symbol=symbol, interval="1m", limit=50)

    df = pd.DataFrame(klines, columns=[
        "time", "open", "high", "low", "close", "volume",
        "_", "_", "_", "_", "_", "_"
    ])

    df["close"] = df["close"].astype(float)

    st.line_chart(df["close"])

except:
    st.warning("Chart unavailable")

# ================= BUTTON =================
st.markdown("---")

if st.button("🚀 Place Order"):

    try:
        logger.info(f"UI Input | {symbol} | {side} | {order_type} | qty={quantity}")

        validate_order(symbol, side, order_type, quantity, price)

        if live_price:
            current_price = price if order_type == "LIMIT" else live_price
            notional = quantity * current_price

            if notional < 100:
                st.error("❌ Below 100 USDT")
                st.stop()

        # --- EXECUTE ---
        if order_type == "MARKET":
            result = place_market_order(symbol, side, quantity)
        else:
            result = place_limit_order(symbol, side, quantity, price)

        logger.info(f"Order Success | {result['orderId']}")

        # --- STORE HISTORY ---
        st.session_state.history.append({
            "Symbol": symbol,
            "Side": side,
            "Type": order_type,
            "Qty": quantity,
            "Status": result["status"]
        })

        st.success("✅ Order Placed")

    except Exception as e:
        logger.error(f"UI Error | {str(e)}")
        st.error(f"❌ {e}")

# ================= ORDER HISTORY =================
st.subheader("📜 Order History")

if st.session_state.history:
    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history)
else:
    st.info("No orders yet")

# ================= AUTO REFRESH =================
time.sleep(refresh_rate)
st.rerun()