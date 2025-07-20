import requests

LIMIT_URL = "http://159.89.165.196:5003/sample_limits"

def get_limits():
    try:
        response = requests.get(LIMIT_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return float(data['high']), float(data['low'])
    except Exception as e:
        print(f"Error fetching limits: {e}")
    return 30.0, 20.0  # fallback defaults
