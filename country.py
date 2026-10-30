import requests

# CountriesNow public API configuration
url_capital = "https://countriesnow.space"
url_population = "https://countriesnow.space"
url_currency = "https://countriesnow.space"

# Ensure precise matching string for the payload
payload = {"country": "Kenya"}

print("Sending request to a free, public country API directory...")

try:
    # 1. Fetch Capital Data
    res_capital = requests.post(url_capital, json=payload)
    data_capital = res_capital.json()
    
    # 2. Fetch Population Data
    res_population = requests.post(url_population, json=payload)
    data_population = res_population.json()
    
    # 3. Fetch Currency Data
    res_currency = requests.post(url_currency, json=payload)
    data_currency = res_currency.json()

    # Check if the API returned an operational error message
    if data_capital.get("error") or data_population.get("error") or data_currency.get("error"):
        print("\n--- API Error Encountered ---")
        print("Capital API Response:", data_capital.get("msg"))
        print("Population API Response:", data_population.get("msg"))
        print("Currency API Response:", data_currency.get("msg"))
    else:
        # Safely drill down using .get() to prevent unexpected KeyError crashes
        cap_info = data_capital.get("data", {})
        pop_info = data_population.get("data", {})
        cur_info = data_currency.get("data", {})

        name = cap_info.get("name", "Kenya")
        capital = cap_info.get("capital", "N/A")
        currency = cur_info.get("currency", "N/A")
        
        # Extrapolate the most recent demographic metrics from the array
        pop_counts = pop_info.get("populationCounts", [])
        latest_population = pop_counts[-1].get("value", 0) if pop_counts else "N/A"

        print("\n=== Success! Country Information ===")
        print(f"Country Name : {name}")
        print(f"Capital City : {capital}")
        if isinstance(latest_population, int):
            print(f"Population   : {latest_population:,}")
        else:
            print(f"Population   : {latest_population}")
        print(f"Currency Code: {currency}")

except Exception as e:
    print("\nA structural Python error occurred during runtime operation:", str(e))
