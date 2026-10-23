"""
Kenyan Business Currency Tracker (KES Converter)

This command-line utility provides international client invoicing clarity for 
Kenyan companies by pulling live forex exchange benchmarks. If the network is 
blocked by a firewall, it safely falls back to reliable local backup benchmarks.

Requirements:
    - requests (Optional fallback uses built-in modules)

How to Run:
    python kes_currency_tracker.py
"""

import json
import os
import requests


def get_live_rates():
    """Fetches real-time base currency conversion tables from open endpoints with structural fallbacks."""
    url = "https://exchangerate-api.com"
    
    # Fallback backup matrix data in case the network/firewall drops entirely
    backup_rates = {
        "USD": 0.0078,  # Approximate benchmark: 1 KES = ~0.0078 USD
        "EUR": 0.0072,  # Approximate benchmark: 1 KES = ~0.0072 EUR
        "GBP": 0.0060   # Approximate benchmark: 1 KES = ~0.0060 GBP
    }
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("rates", backup_rates)
    except Exception:
        # Silently catch network drops and seamlessly switch to backup constants
        pass
        
    print("\n[Notice]: Network restriction detected. Utilizing local fallback business exchange benchmarks.")
    return backup_rates


def save_transaction_log(amount_kes, converted_values, filename="currency_quotes.json"):
    """Appends transactions into local data storage records for accounting history."""
    log_entry = {
        "amount_kes": amount_kes,
        "conversions": converted_values
    }
    
    history = []
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                history = json.load(f)
                if not isinstance(history, list):
                    history = []
        except (IOError, json.JSONDecodeError):
            history = []

    history.append(log_entry)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)
        print(f"💾 Quote snapshot appended cleanly to local ledger database: {filename}")
    except IOError:
        print(f"[Warning]: Failed to persist transaction data snapshot to storage disk.")


def run_tracker():
    """Main application flow routine sequence loop."""
    print("=======================================")
    print("  🇰🇪  KENYAN BUSINESS CURRENCY TRACKER ")
    print("=======================================")

    user_input = input("Enter invoice amount in KES (e.g. 15000): ").strip()
    
    try:
        amount_kes = float(user_input)
        if amount_kes <= 0:
            print("❌ Error: Invoice totals must be greater than zero.")
            return
    except ValueError:
        print(f"❌ Error: '{user_input}' is not a valid number. Avoid commas or text suffixes.")
        return

    print("\nFetching current global exchange tables... Please wait.")
    rates = get_live_rates()

    # Extract required target currency factors safely
    usd_rate = rates.get("USD")
    eur_rate = rates.get("EUR")
    gbp_rate = rates.get("GBP")

    # Calculate multi-currency processing yields
    converted = {
        "USD": round(amount_kes * usd_rate, 2),
        "EUR": round(amount_kes * eur_rate, 2),
        "GBP": round(amount_kes * gbp_rate, 2)
    }

    # Save transaction record locally to JSON database
    save_transaction_log(amount_kes, converted)

    # Format output tables beautifully for business stakeholders
    print(f"\n=== 📊 Invoice Quote Summary ===")
    print(f"• Base Value  : {amount_kes:,.2f} KES")
    print(f"--------------------------------")
    print(f"• US Dollar   : $ {converted['USD']:,.2f} USD")
    print(f"• Euro Zone   : € {converted['EUR']:,.2f} EUR")
    print(f"• British Pnd : £ {converted['GBP']:,.2f} GBP")
    print("=======================================\n")


if __name__ == "__main__":
    run_tracker()
