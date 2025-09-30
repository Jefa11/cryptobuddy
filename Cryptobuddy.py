# Rule-Based Crypto Chatbot with Real-Time Data (CoinGecko API)
# -------------------------------------------------------------

import requests

# 1. Personality & Setup
bot_name = "CryptoBuddy"
disclaimer = "⚠️ Disclaimer: Crypto is risky—always do your own research before investing!"

def intro():
    print(f"👋 Hey! I’m {bot_name}—your friendly crypto guide.")
    print("I’ll help you explore coins based on profitability 🚀 and sustainability 🌱.")
    print(disclaimer)
    print("-" * 60)

# 2. Fetch Real-Time Data (CoinGecko)
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano",  # we can expand this list
        "price_change_percentage": "24h"
    }
    response = requests.get(url, params=params).json()

    # Map CoinGecko data to our structure
    crypto_db = {}
    for coin in response:
        name = coin["name"]
        price_change = coin["price_change_percentage_24h"]
        market_cap = coin["market_cap"]

        # Price trend
        if price_change > 0.5:
            trend = "rising"
        elif price_change < -0.5:
            trend = "falling"
        else:
            trend = "stable"

        # Sustainability (static assumptions for demo)
        if name == "Bitcoin":
            energy_use, sustainability = "high", 3/10
        elif name == "Ethereum":
            energy_use, sustainability = "medium", 6/10
        elif name == "Cardano":
            energy_use, sustainability = "low", 8/10
        else:
            energy_use, sustainability = "unknown", 5/10

        # Market cap level
        if market_cap > 100e9:
            mc_level = "high"
        elif market_cap > 10e9:
            mc_level = "medium"
        else:
            mc_level = "low"

        crypto_db[name] = {
            "price_trend": trend,
            "market_cap": mc_level,
            "energy_use": energy_use,
            "sustainability_score": sustainability
        }
