'''Its job is simply:

Get visible windows
Get PID
Get process name
Get window title
Return data'''


import subprocess
import psutil
def get_visible_windows():
    """
    Returns a list of visible windows with:
    pid
    process_name
    window_title
    executable_path
    """

    windows = []
    try:
        result = subprocess.run(
            ["wmctrl", "-lp"],
            capture_output=True,
            text=True
        )
        for line in result.stdout.splitlines():
            parts = line.split(None, 4)
            if len(parts) < 5:
                continue
            window_id = parts[0]
            pid = parts[2]
            title = parts[4]
            try:
                pid = int(pid)
                process = psutil.Process(pid)
                windows.append({
                    "window_id": window_id,
                    "pid": pid,
                    "process_name": process.name(),
                    "exe_path": process.exe(),
                    "window_title": title
                })
            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                ValueError
            ):
                continue
    except FileNotFoundError:
        print("wmctrl not installed")
    return windows
