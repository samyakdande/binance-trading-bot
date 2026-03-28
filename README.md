# 🚀 Binance Futures Trading Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Binance-Testnet-F0B90B?style=for-the-badge&logo=binance&logoColor=white" />
</p>

<p align="center">
  A modular, production-style trading bot for <strong>Binance Futures Testnet</strong> — featuring a CLI, real-time Streamlit dashboard, structured logging, and Docker support.
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Setup](#-setup)
- [Usage](#-usage)
  - [CLI](#-cli)
  - [Streamlit Dashboard](#-streamlit-dashboard)
  - [Docker](#-docker)
- [Logging](#-logging)
- [Assumptions](#-assumptions)
- [Future Enhancements](#-future-enhancements)

---

## 🌟 Overview

This project provides a clean, extensible foundation for algorithmic trading on the Binance Futures Testnet. It supports both a command-line interface for scripted execution and an interactive web dashboard for real-time monitoring and order placement.

---

## ⚡ Features

| Category | Highlights |
|----------|-----------|
| 📈 Trading | MARKET & LIMIT orders, BUY/SELL support, real-time price integration |
| 🖥️ Dashboard | Live price auto-refresh, price charts, order history, smart validation |
| 🧱 Backend | Modular architecture, reusable services, structured logging |
| 🐳 DevOps | Dockerized execution, environment-based configuration |

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/                    # Core business logic
│   ├── client.py           # Binance API client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logging setup
│
├── app.py                  # Streamlit dashboard
├── cli.py                  # CLI entry point
├── config.py               # Configuration loader
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container definition
└── logs/
    └── bot.log             # Runtime logs
```

---

## 🧠 Architecture

```
        ┌─────────────────────┐
        │    CLI  /  UI       │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │     Validators      │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │    Orders Layer     │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │   Binance Client    │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │    Binance API      │
        └─────────────────────┘

  All layers → logs/bot.log
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd trading_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API keys

Create a `.env` file in the project root:

```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

> ⚠️ Make sure to use **Binance Futures Testnet** credentials, not live keys.

---

## 🚀 Usage

### � CLI

**MARKET order:**

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

**LIMIT order:**

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
```

---

### 🖥️ Streamlit Dashboard

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

The dashboard provides:
- 📊 Live price updates with auto-refresh
- 📈 Price charts
- 📜 Order history tracking
- ⚠️ Real-time validation feedback

---

### 🐳 Docker

**Build the image:**

```bash
docker build -t trading-bot .
```

**Run a container:**

```bash
docker run --env-file .env -v ${PWD}/logs:/app/logs trading-bot \
  --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

## 📄 Logging

Logs are written to `logs/bot.log` and follow a structured format:

```
INFO  | CLI Input     | symbol=BTCUSDT
INFO  | Placing MARKET order
INFO  | Order Success | ID=12345
INFO  | UI Order Success
```

---

## ⚠️ Assumptions

- Binance Futures **Testnet** is used — no real funds are at risk
- Minimum order value is **≥ 100 USDT**
- Valid API credentials must be provided via `.env`

---

## 🔮 Future Enhancements

- [ ] Advanced candlestick charts
- [ ] PnL tracking and reporting
- [ ] Retry logic with exponential backoff
- [ ] Database integration for order persistence
- [ ] WebSocket live price feeds

---

## 👨‍💻 Author

Built as part of a Python Developer assignment.
