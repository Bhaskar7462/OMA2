import requests

def get_coordinates(city):

    url = (
        # here geocoding is used to find the coordinates of the city
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}"
        f"&count=1"
    )

    response = requests.get(url)
    data = response.json()
    if "results" not in data:
        return None
    result = data["results"][0]

    return {
        "name": result["name"],
        "country": result.get("country", "unknown"),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_weather(city):
    location = get_coordinates(city)
    if location is None:
        return None

    latitude = location["latitude"]
    longitude = location["longitude"]
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    response = requests.get(url)
    data = response.json()
    current = data["current"]

    return {
        "city": location["name"],
        "country": location["country"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"]
    }