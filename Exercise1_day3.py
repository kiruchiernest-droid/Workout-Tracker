"""
Travel Weather & Country Information Tool

This script fetches current weather conditions from the OpenWeather API 
and global region metrics from the RestCountries API based on user location input.
It merges both datasets and caches the result into a local JSON file.

Requirements:
    - python-dotenv
    - requests

Setup:
    Create a `.env` file in your project folder containing:
    OPENWEATHER_API_KEY=your_actual_api_key_here

How to Run:
    python day3_travel_info.py
"""

import json
import os
import requests
from dotenv import load_dotenv

# Standard dynamic configuration initialization
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """Fetches live meteorological updates for a specified city."""
    if not API_KEY:
        print("\n[Error]: Missing configuration. Please verify your .env file contains an API_KEY.")
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("\n[Error]: Unauthorized API Key. Please verify your OpenWeather key details.")
    except requests.exceptions.RequestException:
        print("\n[Error]: System connection timeout while reaching the weather database.")
    return None


def get_country_info(country_code):
    """Fetches geographic profile metrics utilizing standardized country codes."""
    # Corrected path to point safely to the alpha code search directory
    url = f"https://restcountries.com{country_code}"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return data[0] if isinstance(data, list) else data
    except requests.exceptions.RequestException:
        print("\n[Warning]: Failed to connect to regional context registry databases.")
    return None


def save_to_file(data, filename):
    """Writes combined structural profile details out to structured JSON stores."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"💾 Record saved successfully to: {filename}")
    except IOError:
        print(f"\n[Error]: System permission restrictions prevented writing data to {filename}.")


def run_tool():
    """Executes main application loop logic sequence pipeline routines."""
    print("=======================================")
    print("       ✈️  TRAVEL WEATHER TOOL  ☀️      ")
    print("=======================================")
    
    city = input("Enter a destination city name: ").strip()

    if not city:
        print("❌ No input detected. Operation cancelled.")
        return

    print(f"\nSearching data registries for '{city}'...")
    weather_data = get_weather(city)

    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the spelling and try again.")
        return

    # Extract country properties safely
    country_code = weather_data.get("sys", {}).get("country")
    country_data = get_country_info(country_code)

    # COMBINE RESULTS: Merge both API payloads into a single structured report dictionary
    combined_report = {
        "search_query": city,
        "weather_metrics": weather_data,
        "country_profile": country_data
    }

    # Save the combined dataset to a clean JSON file
    file_target = f"{city.lower().replace(' ', '_')}_travel_report.json"
    save_to_file(combined_report, file_target)

    # Format clean, highly readable output presentation layouts for non-technical users
    print(f"\n=== 📍 {city.title()}, {country_code} ===")
    print(f"• Temperature : {weather_data['main']['temp']}°C")
    print(f"• Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"• Humidity    : {weather_data['main']['humidity']}%")
    print(f"• Wind Speed  : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population", 0)
        region = country_data.get("region", "Unknown Sub-Continent")
        
        # Safely extract currency name mapping fields
        currency_block = country_data.get("currencies", {})
        currency_names = [details.get("name") for details in currency_block.values() if "name" in details]
        currency_output = ", ".join(currency_names) if currency_names else "N/A"

        print(f"\n=== 🌐 Regional Context ===")
        print(f"• Continent   : {region}")
        print(f"• Population  : {population:,} citizens")
        print(f"• Currency    : {currency_output}")
    print("=======================================\n")


if __name__ == "__main__":
    run_tool()
