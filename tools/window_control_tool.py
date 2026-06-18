import subprocess


def maximize_window(window_id):

    # Maximize a window.

    subprocess.run(
        [
            "wmctrl",
            "-ir",
            window_id,
            "-b",
            "add,maximized_vert,maximized_horz"
        ],
        check=False
    )


def minimize_window(window_id):

    # Minimize (hide) a window.

    subprocess.run(
        [
            "wmctrl",
            "-ir",
            window_id,
            "-b",
            "add,hidden"
        ],
        check=False
    )


def restore_window(window_id):

    # Restore a maximized window to normal size.

    subprocess.run(
        [
            "wmctrl",
            "-ir",
            window_id,
            "-b",
            "remove,maximized_vert,maximized_horz"
        ],
        check=False
    )


def focus_window(window_id):
    
    # Bring a window to the foreground and focus it.

    subprocess.run(
        [
            "wmctrl",
            "-ia",
            window_id
        ],
        check=False
    )