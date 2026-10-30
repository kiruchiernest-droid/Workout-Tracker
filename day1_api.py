import requests

# Updated endpoint URL for version 5
url = "https://restcountries.com"

# The v5 API requires an API key in the Authorization header
headers = {
    "Authorization": "Bearer rc_live_demo"
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Data received:", response.json())
