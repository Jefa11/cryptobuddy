# CryptoBuddy

Lightweight rule-based crypto assistant that fetches live data from CoinGecko and prints a short summary for a small set of coins (Bitcoin, Ethereum, Cardano).

## Requirements
- Python 3.8+
- The `requests` package

Install dependencies (PowerShell):

```powershell
python -m pip install --user requests
```

## Run
From PowerShell run:

```powershell
python Cryptobuddy.py
```

You should see an intro and a JSON summary similar to:

```json
{
  "Bitcoin": {
    "price_trend": "rising",
    "market_cap_level": "high",
    "energy_use": "high",
    "sustainability_score": 0.3,
    "raw_market_cap": 2272407011878.0,
    "raw_price_change_24h": 2.03034
  },
  "Ethereum": { ... },
  "Cardano": { ... }
}
```

## What it does
- Calls the CoinGecko `/coins/markets` endpoint for `bitcoin,ethereum,cardano`.
- Normalizes fields and classifies price trend and market-cap level.
- Adds a small static "sustainability" score for demo purposes.

## Troubleshooting
- If you get a network/API error: ensure you have an internet connection and CoinGecko is reachable.
- If `requests` is missing: install it using the command above.
- If you want to fetch different coins, edit the `ids` parameter in `fetch_crypto_data()` inside `Cryptobuddy.py`.

## Next steps (ideas)
- Make the coin list a CLI argument.
- Pretty-print the output as a table.
- Add caching and rate-limit handling for the CoinGecko API.

---


`Cryptobuddy.py` was updated to add error handling and a runnable `main()` during debugging.
