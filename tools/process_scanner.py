import psutil


def get_running_processes():
    """
    Returns information about all running processes.
    """

    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'exe']
    ):
        try:

            pid = process.info['pid']
            name = process.info['name'] or ""
            exe_path = process.info['exe'] or ""
            if not exe_path:
                continue

            search_text = (
                name + " " + exe_path
            ).lower()

            processes.append({
                "pid": pid,
                "process_name": name,
                "exe_path": exe_path,
                "search_text": search_text
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return processes