# Travel Weather & Country Information Tool

A lightweight, reliable command-line application that acts as a destination companion by pulling live updates from multiple global endpoints simultaneously.

## 🛠️ The Problem It Solves
When traveling or researching a city, checking separate sources for climate conditions and essential country logistics (like currencies or local population indexes) is tedious. This utility solves that friction by pulling live metrics from multiple open-data APIs simultaneously, combining the structures, and exporting them cleanly for storage.

## 🚀 Features
- **Live Weather Updates:** Pulls temperature, wind metrics, and clear conditions from OpenWeather.
- **Contextual Country Profiles:** Maps country keys immediately to fetch currency descriptors and local statistics.
- **Automated Data Persistence:** Packages responses into structured, cleanly indented local JSON files.
- **Fail-Safe Integrity:** Captures typos, invalid API signatures, and unexpected internet dropping without crashing.

## 💻 Installation & Setup

1. **Install Project Dependencies:**
   Make sure you have your dependencies installed via terminal:
   ```bash
   pip install requests python-dotenv
   ```

2. **Configure Your API Access Environment:**
   Create a file exactly named `.env` in the root folder of this project, and save your individual development credentials into it:
   ```text
   OPENWEATHER_API_KEY=your_actual_32_character_api_key_here
   ```

3. **Launch the Application Execution Routine:**
   Execute the central script using Python:
   ```bash
   python Exercise1_day3.py
   ```
