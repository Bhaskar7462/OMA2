import subprocess
from tools.app_scanner import get_installed_apps
def open_app(app_name):
    installed_apps = get_installed_apps()
    app_name = app_name.lower()
    desktop_id = None
    display_name = None
    for name, app_id in installed_apps.items():
        if app_name in name.lower():
            display_name = name
            desktop_id = app_id
            break
    if not desktop_id:
        return f"Sorry Boss, I couldn't find '{app_name}'."
    try:
        subprocess.Popen(
            ["gtk-launch", desktop_id]
        )
        return f"Opening {display_name}..."
    except Exception as e:
        return f"Error: {e}"