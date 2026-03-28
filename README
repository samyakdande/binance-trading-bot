# 🚀 Binance Futures Trading Bot (Testnet)

A modular Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet with:

* CLI interface
* Streamlit dashboard
* Structured logging
* Dockerized deployment

---

## 📌 Features

* ✅ MARKET & LIMIT order execution
* ✅ BUY and SELL support
* ✅ CLI interface (argparse)
* ✅ Streamlit UI dashboard
* ✅ Real-time price auto-refresh
* ✅ Order history tracking
* ✅ Price charts (candlestick trend)
* ✅ Input validation (≥100 USDT rule)
* ✅ Structured logging
* ✅ Docker support

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── .env
└── logs/
    └── bot.log
```

---

## 🧠 Architecture

```
CLI / Streamlit UI
        ↓
   Validators
        ↓
   Orders Layer
        ↓
   Binance Client
        ↓
 Binance Futures API

Logging:
All layers → logs/bot.log
```

---

## ⚙️ Setup

### 1. Clone repo

```
git clone <your-repo-url>
cd trading_bot
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add API keys

Create `.env`:

```
API_KEY=your_testnet_key
API_SECRET=your_testnet_secret
```

⚠️ Use Binance Futures Testnet keys

---

## ▶️ Run CLI

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
```

---

## 🖥️ Run Streamlit UI

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

### UI Features:

* Live price auto-refresh
* Order placement
* Validation feedback
* Order history table
* Price charts

---

## 🐳 Run with Docker

### Build

```
docker build -t trading-bot .
```

### Run

```
docker run --env-file .env -v ${PWD}/logs:/app/logs trading-bot --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

## 📄 Logging

Logs stored in:

```
logs/bot.log
```

### Example

```
INFO | CLI Input | symbol=BTCUSDT
INFO | Placing MARKET order
INFO | Order Success | ID=12345
INFO | UI Order Success
```

---

## ⚠️ Assumptions

* Binance Futures Testnet used
* Min order size ≥ 100 USDT
* Internet required

---

## 🧠 Design Decisions

* Modular architecture
* Separation of concerns
* Reusable backend for CLI & UI
* Centralized logging
* Docker for portability

---

## 🚀 Future Improvements

* Stop-Limit / OCO orders
* Trade history persistence (DB)
* Advanced charts (candlestick UI)
* PnL tracking

---

## 👨‍💻 Author

Developed as part of a Python Developer assignment.
