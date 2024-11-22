import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")
def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    nr_values = 8 * forecast_days
    filtered_content = filtered_content[:nr_values]
    if kind == "Temperature":
        filtered_content = [dict["main"]["temp"] for dict in filtered_content]
    elif kind == "Sky":
        filtered_content = [dict["weather"][0]["main"] for dict in filtered_content]
    return filtered_content

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))