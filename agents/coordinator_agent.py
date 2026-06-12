from agents.system_agent import system_agent
from agents.llm_agent import llm_agent
from agents.weather_agent import weather_agent
from agents.app_agent import app_agent
from agents.close_app_agent import close_app_agent


def extract_city(user_input):
    keywords = [
        "weather in",
        "temperature in",
        "forecast in",
        "wind in",
        "humidity in",
    ]

    for keyword in keywords:
        if keyword in user_input:
            city = user_input.split(keyword)[1].strip()
            return city

    return None


def extract_app(user_input):
    if user_input.startswith("open "):
        return user_input.replace("open ", "").strip()

    return None


def extract_close_app(user_input):
    if user_input.startswith("close "):
        return user_input.replace("close ", "").strip()

    if user_input.startswith("exit "):
        return user_input.replace("exit ", "").strip()

    return None


def coordinator_agent(user_input):
    user_input = user_input.lower()

    system_keywords = [
        "system",
        "cpu",
        "ram",
        "battery",
        "memory"
    ]

    weather_keywords = [
        "weather",
        "temperature",
        "humidity",
        "forecast",
        "wind"
    ]

    # System Agent Routing
    for keyword in system_keywords:
        if keyword in user_input:
            return system_agent()

    # Weather Agent Routing
    for keyword in weather_keywords:
        if keyword in user_input:
            city = extract_city(user_input)

            if city:
                return weather_agent(city)

            return weather_agent("Delhi")

    # App Closing Routing
    if (
        user_input.startswith("close ")
        or user_input.startswith("exit ")
    ):
        app_name = extract_close_app(user_input)

        if app_name:
            return close_app_agent(app_name)

    # App Launcher Routing
    if user_input.startswith("open "):
        app_name = extract_app(user_input)

        if app_name:
            return app_agent(app_name)

    # Default LLM Agent
    return llm_agent(user_input)