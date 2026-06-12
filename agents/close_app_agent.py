from tools.app_candidates import (get_all_candidates)
from tools.smart_matcher import (find_best_match)
from tools.close_app_tool import (close_process)


def close_app_agent(app_name):

    candidates = get_all_candidates()

    best_app, matches = find_best_match(
        app_name,
        candidates
    )

    if not best_app:
        return (
            f"Sorry Boss, I couldn't find "
            f"any running application matching '{app_name}'."
        )

    process_name = best_app[
        "process_name"
    ]

    closed = close_process(
        process_name
    )

    if closed:
        return (
            f"Closed: {process_name}"
        )

    return (
        f"Found '{process_name}' "
        f"but could not close it."
    )