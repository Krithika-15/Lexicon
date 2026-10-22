from pprint import pprint
from api_client import get_json
import json
import os, time

GEO_URL ="https://geocoding-api.open-meteo.com/v1/search"

# 1. Find coordinates of a city
# data = get_json(GEO_URL, params={"name": "Stockholm", "count":1})
# # pprint(data)
# city = data["results"][0]
# latitude = city["latitude"]
# longitude = city["longitude"]
# print(f"latitude : {latitude}\nlongitude : {longitude}")


def find_city(name):
    data = get_json(GEO_URL, params={"name":name, "count":1})

    # request failed (no internet or timeout)
    if data is None:
        return None

    city = data.get("results")

    # no city with that name
    if not city:
        return None

    return city[0]



# 2. get the weather for those coordinates
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
CURRENT_FIELDS  = "temperature_2m,wind_speed_10m"
# data = get_json(FORECAST_URL, params={"latitude":latitude, "longitude":longitude, "current":CURRENT_FIELDS })
# pprint(data)

def get_weather(latitude, longitude, current):
    data = get_json(FORECAST_URL, params={"latitude":latitude, "longitude":longitude, "current":current, "timezone": "auto"})
    return data


# Use the file when it is fresh
# print(os.path.exists("weather.json"))
# print(os.path.getmtime("weather.json"))
# print(time.time())
# print(time.time() - os.path.getmtime("weather.json"))

def show_weather(city, weather):
    current = weather["current"]
    current_units = weather["current_units"]

    temperature = current["temperature_2m"]
    temp_units = current_units["temperature_2m"]
    wind = current["wind_speed_10m"]
    wind_units = current_units["wind_speed_10m"]
    country = city["country"]
    city_name = city["name"]

    print(f"{city_name}, {country}: {temperature}{temp_units}, wind {wind} {wind_units}")


CACHE_FILE = "weather.json"
MAX_FILE_AGE = 600

if os.path.exists(CACHE_FILE) and time.time() - os.path.getmtime(CACHE_FILE) < MAX_FILE_AGE:
    print("(From cache)")
    with open(CACHE_FILE, encoding="utf-8") as f:
        data = json.load(f)
    show_weather(data["city"], data["weather"])
else:
    print("(From API)")
    # 3. Put it together
    user_input_city = input("Enter the city name : ")
    city = find_city(user_input_city)
    # pprint(city)
    if city is None:
        print("Sorry, Could not find that city")
    else:
        latitude = city["latitude"]
        longitude = city["longitude"]

        weather = get_weather(latitude, longitude, CURRENT_FIELDS)
        # pprint(weather)
        if weather is None:
            print("Sorry, Could not get the weather")
        else:
            show_weather(city, weather)
            data = {"city": city, "weather": weather}
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)




# 1
# notes
# with open opens file if already exists and wipes completely before writing,
# or creates if doesn't exist. Then after writing closes file even program crashes in between
# Then json.dump turns Python dict into JSON text and writes to the file
# indent makes look formatted
# ensure_ascii=False keeps real characters instead of escape codes.
# To be safe on windows encoding="utf-8" tells file to accept the characters (output of above line)
# By default json.dump writes °C as \u00b0C and Göteborg as G\u00f6teborg => valid JSON, but unreadable
# With this off, we get °C and Göteborg as themselves



# Explain why?
# Open-Meteo recalculates every 15 minutes, so any calls within that time returns same answer twice.
# Rate limits : GitHub: 60/hour anonymous, 5000 with a token, so cached read will cost zero request.
# Reading a local file is faster, than a network call with DNS lookup, TCP connection, TLS handshake, round trip, parsing.
# It works even when network is down.
# After program closes all values are gone, so saving in a file is best way to pass what it got earlier before the program closed.
# Trade Off :
# data might be old upto 600 second (10 minutes)
# when we want to check for another city the program doesn't prompt and shows same old city name for 10 minutes
# need to store one file per city or one file holding a dict keyed by city name
