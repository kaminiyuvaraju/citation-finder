import requests

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)  # Increase timeout to 10 seconds
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()['results']
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []  # Return an empty list if fetching data fails
