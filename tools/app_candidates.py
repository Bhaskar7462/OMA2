# it is for merging the output from the window matcher and process matcher
from tools.window_scanner import (
    get_visible_windows
)

from tools.process_scanner import (get_running_processes)


def get_all_candidates():
    candidates = []
    windows = get_visible_windows()
    seen_pids = set()

    # Visible Windows
    for window in windows:
        candidates.append(window)
        seen_pids.add(
            window["pid"]
        )

    # Background Processes
    processes = get_running_processes()
    for process in processes:
        if process["pid"] in seen_pids:
            continue
        candidates.append({
            "pid":
            process["pid"],
            "process_name":
            process["process_name"],
            "exe_path":
            process["exe_path"],
            "window_title":
            ""
        })
    return candidates