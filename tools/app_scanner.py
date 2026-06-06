import os
def get_installed_apps():
    apps = {}
    folders = [
        "/usr/share/applications",
        "/var/lib/snapd/desktop/applications",
        os.path.expanduser("~/.local/share/applications")
    ]
    for folder in folders:
        if not os.path.exists(folder):
            continue
        for file in os.listdir(folder):
            if not file.endswith(".desktop"):
                continue
            desktop_id = file.replace(".desktop", "")
            desktop_file = os.path.join(folder, file)
            try:
                with open(desktop_file, "r", encoding="utf-8") as f:
                    app_name = None
                    for line in f:
                        if line.startswith("Name="):
                            app_name = line.replace("Name=", "").strip()
                            break
                    if app_name:
                        apps[app_name] = desktop_id
            except Exception:
                pass
    return apps