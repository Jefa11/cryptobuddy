# Rule-Based Crypto Chatbot with Real-Time Data (CoinGecko API)
# -------------------------------------------------------------

import requests

"""
Rule-Based Crypto Chatbot with Real-Time Data (CoinGecko API)
"""

import json
import requests
from typing import Dict, Any

# 1. Personality & Setup
bot_name = "CryptoBuddy"
disclaimer = "⚠️ Disclaimer: Crypto is risky—always do your own research before investing!"


def intro() -> None:
    print(f"👋 Hey! I’m {bot_name}—your friendly crypto guide.")
    print("I’ll help you explore coins based on profitability 🚀 and sustainability 🌱.")
    print(disclaimer)
    print("-" * 60)


def fetch_crypto_data() -> Dict[str, Any]:
    """Fetches a small set of coins from CoinGecko and returns a normalized dict.

    Returns an empty dict on error and prints a helpful message.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano",
        "price_change_percentage": "24h"
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"Network/API error while fetching data: {exc}")
        return {}

    try:
        data = resp.json()
        if not isinstance(data, list):
            print("Unexpected API response format: expected a list")
            return {}
    except ValueError:
        print("Failed to decode JSON from CoinGecko response")
        return {}

    crypto_db: Dict[str, Any] = {}
    for coin in data:
        # use .get with defaults to avoid KeyError
        name = coin.get("name", coin.get("id", "unknown")).title()
        price_change = coin.get("price_change_percentage_24h")
        market_cap = coin.get("market_cap")

        # handle missing numeric fields
        try:
            price_change = float(price_change) if price_change is not None else 0.0
        except (TypeError, ValueError):
            price_change = 0.0

        try:
            market_cap = float(market_cap) if market_cap is not None else 0.0
        except (TypeError, ValueError):
            market_cap = 0.0

        if price_change > 0.5:
            trend = "rising"
        elif price_change < -0.5:
            trend = "falling"
        else:
            trend = "stable"

        # Sustainability (static assumptions for demo)
        if name.lower().startswith("bitcoin"):
            energy_use, sustainability = "high", 3 / 10
        elif name.lower().startswith("ethereum"):
            energy_use, sustainability = "medium", 6 / 10
        elif name.lower().startswith("cardano"):
            energy_use, sustainability = "low", 8 / 10
        else:
            energy_use, sustainability = "unknown", 5 / 10

        if market_cap > 100e9:
            mc_level = "high"
        elif market_cap > 10e9:
            mc_level = "medium"
        else:
            mc_level = "low"

        crypto_db[name] = {
            "price_trend": trend,
            "market_cap_level": mc_level,
            "energy_use": energy_use,
            "sustainability_score": sustainability,
            "raw_market_cap": market_cap,
            "raw_price_change_24h": price_change,
        }

    return crypto_db


def main() -> None:
    intro()
    data = fetch_crypto_data()
    if not data:
        print("No data available. See messages above for errors.")
        return

    print("Fetched coin summaries:")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
