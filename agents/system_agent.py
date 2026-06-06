from tools.system_tool import get_system_info

def system_agent():
    info = get_system_info()

    response = f"""
System Status
CPU usage: {info['cpu_usage']}%
RAM Usage: {info['memory_usage']}%
Battery: {info['battery']}%
"""

    return response




