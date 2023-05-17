import requests
import pandas as pd

def get_weather_forecast(api_key, cities):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    forecasts = []

    for city in cities:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        try:
            response = requests.get(base_url, params=params)
            weather_data = response.json()

            if weather_data["cod"] == 200:
                forecast = {
                    "City": weather_data["name"],
                    "Temperature (°C)": weather_data["main"]["temp"],
                    "Humidity (%)": weather_data["main"]["humidity"],
                    "Description": weather_data["weather"][0]["description"]
                }
                forecasts.append(forecast)
            else:
                print(f"Error fetching weather data for {city}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    df = pd.DataFrame(forecasts)
    print(df)

# Set your OpenWeatherMap API key
API_KEY = "8cc0959a1d55e0b4a89883f084d443c1"

# Set the cities for weather forecast
# cities = input("Enter the city: ")
City_array = input("Enter one or more cities name : ")
cities = City_array.split()


# Get the weather forecast for cities
get_weather_forecast(API_KEY, cities)