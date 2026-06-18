'''
flow of window control

User Input
    ↓
Coordinator
    ↓
Window Control Agent
    ↓
find_best_match()
    ↓
Correct PyCharm Window
    ↓
restore_window()
'''



from tools.window_scanner import get_visible_windows
from tools.smart_matcher import find_best_match
from tools.window_control_tool import (
    maximize_window,
    minimize_window,
    restore_window,
    focus_window
)


def handle_window_control(user_input):
    user_input = user_input.lower()

    windows = get_visible_windows()

    if not windows:
        return "No visible windows found."

    action = None

    if "maximize" in user_input:
        action = "maximize"

    elif "minimize" in user_input:
        action = "minimize"

    elif "restore" in user_input:
        action = "restore"

    elif "focus" in user_input:
        action = "focus"

    else:
        return "No window control action detected."

    app_name = (
        user_input
        .replace("maximize", "")
        .replace("minimize", "")
        .replace("restore", "")
        .replace("focus", "")
        .strip()
    )

    best_match, matches = find_best_match(
        app_name,
        windows
    )

    if not best_match:
        return f"Could not find '{app_name}'."

    window_id = best_match["window_id"]

    if action == "maximize":
        maximize_window(window_id)

    elif action == "minimize":
        minimize_window(window_id)

    elif action == "restore":
        restore_window(window_id)

    elif action == "focus":
        focus_window(window_id)

    return (
        f"{action.title()}d "
        f"{best_match['window_title']}"
    )