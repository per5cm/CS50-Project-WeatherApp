import requests
import os
from dataclasses import dataclass

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

def load_api_key():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found.")
    return api_key


def get_lat_lon(city_name, state_code, country_code, API_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={API_key}"
    response = requests.get(url).json()
    
    if not response:
        raise ValueError(f"City: {city_name}, was not found.")

    data = response[0]
    lat, lon = data.get("lat"), data.get("lon")
    return lat, lon

def get_current_weather(lat, lon, API_key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric").json()
    data = WeatherData(
        main=response.get("weather")[0].get("main"),
        description=response.get("weather")[0].get("description"),
        icon=response.get("weather")[0].get("icon"),
        temperature=int(response.get("main").get("temp")),
    )

    return data

def main(city_name, state_name, country_name):
    api_key = load_api_key()
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data

if __name__ == "__main__":
    main()