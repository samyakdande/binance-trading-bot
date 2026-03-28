## ⚙️ Setup

### 1️⃣ Clone Repo

bash
git clone <your-repo-url>
cd trading_bot


---

### 2️⃣ Install Dependencies

bash
pip install -r requirements.txt


---

### 3️⃣ Configure API Keys

Create `.env`:

env
API_KEY=your_testnet_key
API_SECRET=your_testnet_secret

⚠️ Use **Binance Futures Testnet keys**

---

## ▶️ Run CLI

### 🟢 MARKET Order

bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


### 🔵 LIMIT Order

bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000


---

## 🖥️ Run Streamlit Dashboard

bash
streamlit run app.py


📍 Open: http://localhost:8501

### 🔥 UI Highlights

* 📊 Live price updates
* 📈 Charts
* 📜 Order history
* ⚠️ Validation feedback

---

## 🐳 Run with Docker

### Build Image

bash
docker build -t trading-bot .


### Run Container

bash
docker run --env-file .env -v ${PWD}/logs:/app/logs trading-bot --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
