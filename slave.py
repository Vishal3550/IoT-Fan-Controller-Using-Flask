import requests

class Slave:
    def __init__(self, url):
        self.url = url

    def get_temperature(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                return float(response.json()['temperature'])
            else:
                print("Error fetching temperature")
                return None
        except Exception as e:
            print(f"Exception: {e}")
            return None
