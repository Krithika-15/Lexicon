from pprint import pprint
from api_client import get_json

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



# # 2. get the weather for those coordinates
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
CURRENT_FIELDS  = "temperature_2m,wind_speed_10m"
# data = get_json(FORECAST_URL, params={"latitude":latitude, "longitude":longitude, "current":CURRENT_FIELDS })
# pprint(data)

def get_weather(latitude, longitude, current):
    data = get_json(FORECAST_URL, params={"latitude":latitude, "longitude":longitude, "current":current, "timezone": "auto"})
    return data


# 3. Put it together
user_input_city = input("Enter the city name : ")
city = find_city(user_input_city)
# pprint(city)
if city is None:
    print("Sorry, Could not find that city")
else:
    latitude = city["latitude"]
    longitude = city["longitude"]
    country = city["country"]
    city_name = city["name"]

    weather = get_weather(latitude, longitude, CURRENT_FIELDS)
    # pprint(weather)
    if weather is None:
        print("Sorry, Could not get the weather")
    else:
        current = weather["current"]
        current_units = weather["current_units"]

        temperature = current["temperature_2m"]
        temp_units = current_units["temperature_2m"]
        wind = current["wind_speed_10m"]
        wind_units = current_units["wind_speed_10m"]
        print(f"{city_name}, {country}: {temperature}{temp_units}, wind {wind} {wind_units}")

