import subprocess
from tools.app_scanner import get_installed_apps

def find_apps(query):
    installed_apps = get_installed_apps()
    query = query.lower().strip()
    matches = []
    for name, app_id in installed_apps.items():
        score = 0
        app_name = name.lower()
        if app_name == query:
            score += 250

        elif app_name.startswith(query):
            score += 220

        elif query in app_name:
            score += 200
        else:
            continue
        score += max(0, 20 - len(app_name))
        matches.append({
            "type": "application",
            "name": name,
            "desktop_id": app_id,
            "score": score
        })

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matches


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
            ["gtk-launch", desktop_id],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return f"Opening {display_name}..."
    except Exception as e:
        return f"Error: {e}"