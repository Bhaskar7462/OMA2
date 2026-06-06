from tools.weather_tool import get_weather

def weather_agent(city):

    weather = get_weather(city)
    if weather is None:
        return f"Sorry Boss, I couldn't find the weather for {city}."

    response = f"""
Weather Report

City: {weather['city']}
Country: {weather['country']}

Temperature: {weather['temperature']}°C
Humidity: {weather['humidity']}%
Wind Speed: {weather['wind_speed']}km/h
"""
    return response

