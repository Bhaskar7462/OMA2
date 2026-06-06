import psutil
def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    battery_percenta = (round(battery.percent,1) if battery else "Not Available")

    return {
        "cpu_usage": cpu,
        "memory_usage": memory,
        "battery": battery_percenta
    }