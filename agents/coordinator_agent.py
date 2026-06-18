# it is used for coordinating all the agents and tools are called from the agents

from agents.open_agent import open_agent
from agents.system_agent import system_agent
from agents.llm_agent import llm_agent
from agents.weather_agent import weather_agent
from agents.close_app_agent import close_app_agent
from agents.memory_agent import memory_agent
from agents.window_control_agent import handle_window_control

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

    # Window Control Routing
    window_control_keywords = [
        "maximize",
        "minimize",
        "restore",
        "focus"
    ]

    for keyword in window_control_keywords:
        if user_input.startswith(keyword + " "):
            return handle_window_control(user_input)



    # App Launcher Routing
    if (
            user_input.startswith("open ")
            or user_input == "more"
            or user_input.isdigit()
    ):
        return open_agent(user_input)

    # Memory routing
    memory_response = memory_agent(user_input)

    if memory_response is not None:
        return memory_response

    # Default LLM Agent
    return llm_agent(user_input)