# it scannen hole home directory for folder and file
import os

def scan_home_directory():

    scan_paths = [
        os.path.expanduser("~"),
        "/media/Data"
    ]

    results = []

    for scan_path in scan_paths:
        if not os.path.exists(scan_path):
            continue
        for root, dirs, files in os.walk(scan_path):
            for folder in dirs:
                results.append({
                    "name": folder,
                    "path": os.path.join(root, folder),
                    "type": "folder"
                })

            for file in files:
                results.append({
                    "name": file,
                    "path": os.path.join(root, file),
                    "type": "file"
                })

    return results