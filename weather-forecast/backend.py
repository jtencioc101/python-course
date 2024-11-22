import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")
def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    nr_values = 8 * forecast_days
    filtered_content = filtered_content[:nr_values]
    return filtered_content

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))