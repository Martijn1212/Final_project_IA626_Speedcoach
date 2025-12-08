import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"   # change if running on server
API_KEY = "1111"                    # Replace with a valid test key


def pretty_print(title, data):
    print("\n" + "="*50)
    print(title)
    print("="*50)
    print(json.dumps(data, indent=4, default=str))
    print()


def test_getData():
    url = f"{BASE_URL}/getData"
    params = {"key": API_KEY}

    print(f"GET {url} with {params}")

    response = requests.get(url, params=params)

    print(f"Status: {response.status_code}")

    try:
        data = response.json()
        pretty_print("API Response (JSON)", data)
    except Exception:
        print("Raw Response:")
        print(response.text)

if __name__ == "__main__":
    print("\n=== Starting API Test Client ===\n")
    test_getData()
    print("\n=== Testing Completed ===\n")
