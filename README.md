# Heska Agent 🚀

**Heska** is an always-on AI agent that monitors X (Twitter) and catches hot meme coin narratives on Solana before they explode.

---

## What Heska Does

Heska is your **narrative scout** that:

- 📊 **Tracks memecoins narrative heat** using Sharpe Narratives and social data platforms
- 🔥 **Finds trending coins** with exploding social volume on X and other platforms  
- 🆕 **Detects new launches** from influencers via meme-coin tracking tools
- 🧠 **Spots narrative clusters** when multiple coins with similar themes trend together
- ⚡ **Sends you clean alerts** via Telegram with actionable signals

Heska doesn't scrape X directly—it uses stable APIs and dashboards designed for crypto social intelligence.

---

## Core Data Sources

### 1. **Narrative Heat (Macro Level)**
- **Sharpe Narratives** – Tracks when the "Memecoins" sector is heating up or cooling down
- Shows performance, social volume, and trend strength for memecoins as a category

### 2. **Social & X Sentiment (Coin Level)**  
- **LunarCrush** – Social volume, social dominance, trending coins based on X and social platforms
- **xScanr** – Solana meme coin Twitter tracking, new tokens, engagement metrics
- **GMGN.AI** – Links tweet spikes to meme-coin price action

### 3. **New Launches & Influencer Coins**
- Tools that detect new tokens + the X accounts that posted them
- Shows contract address, liquidity, market cap, and original tweet

---

## How Heska Decides Something is "Hot"

### Sector-Level Trigger (Macro)
- If **Memecoins narrative index** > recent average by threshold and rising → "sector warming"

### Coin-Level Trigger
- If a coin's **X mentions and social volume** spike strongly vs 24h baseline → "candidate hot coin"
- Must appear on multiple trackers' trending lists

### Narrative-Level Trigger  
- Multiple new coins share similar keywords/themes (e.g., "penguin", "teacher", "AI") and all show social spikes → **new narrative cluster**

### Extra Boost
- Coins driven by mid-to-big X accounts or influencer launch trackers get **higher priority**

---

## Example Alerts

```
Heska | MEMECOINS HOT
Sharpe shows Memecoins momentum up; social mindshare rising.
```

```
Heska | NEW HOT MEME: $PENG
Social volume + contributors surging on LunarCrush; trend = up.
Check liquidity and holders before entering.
```

```  
Heska | NEW SOL MEME: $TEACHER
Detected on xScanr from verified influencer (250k followers).
Launched 10 min ago | MC: 120k | Liq: 30k
Tweet: [link]
```

---

## Tech Stack (Planned)

- **Language**: Python  
- **Run Location**: VPS (always-on) or Mac with scheduled execution
- **Alert Channel**: Telegram bot
- **APIs/Data**:  
  - Sharpe Narratives API
  - LunarCrush API  
  - xScanr web scraping or API (if available)
  - GMGN.AI tracking

---

## Project Structure (Coming Soon)

```
heska-agent/
├── README.md              # This file
├── heska.py               # Main agent loop
├── config.py              # Configuration and API keys
├── .env.example           # Example environment variables
├── sources/
│   ├── sharpe.py          # Sharpe Narratives integration  
│   ├── lunarcrush.py      # LunarCrush integration
│   └── xscanr.py          # xScanr integration
├── alerts/
│   └── telegram.py        # Telegram bot alert system
└── requirements.txt       # Python dependencies
```

---

## Setup Instructions (Coming Soon)

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with your API keys:
   ```
   SHARPE_API_KEY=your_key
   LUNARCRUSH_API_KEY=your_key  
   TELEGRAM_BOT_TOKEN=your_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```
4. Run Heska: `python heska.py`

---

## Roadmap

- [x] Define Heska's capabilities and data sources  
- [ ] Build Python script with main monitoring loop
- [ ] Integrate Sharpe Narratives API
- [ ] Integrate LunarCrush API  
- [ ] Add xScanr tracking for Solana memes
- [ ] Set up Telegram bot alerts
- [ ] Add basic risk checks (liquidity, holder distribution)
- [ ] Deploy to VPS for 24/7 operation
- [ ] Expand to Base and TON chains

---

## Why "Heska"?

Heska is your personal alpha hunter—always watching, always learning, always ahead of the narrative.

---

## License

MIT License - feel free to fork and build your own version!
