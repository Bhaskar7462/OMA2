import psutil


def close_process(process_name):
    """
    Close all processes matching process_name.
    Returns True if at least one process was closed.
    """

    closed = False

    for process in psutil.process_iter(
        ["pid", "name"]
    ):
        try:
            name = process.info["name"]

            if not name:
                continue

            if name.lower() == process_name.lower():
                process.terminate()
                closed = True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return closed