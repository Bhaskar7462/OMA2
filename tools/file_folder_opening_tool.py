# it is responsible for opening files and folder

#import subprocess

#from file_scanner_tool import scan_home_directory # now it become irrelevent because we are using indexing that usues this function



import subprocess

from tools.file_index_tool import get_file_index
from tools.file_matcher_tool import find_matches

def find_files_and_folders(query):
    items = get_file_index()
    matches = find_matches(query, items)
    results = []
    for match in matches:
        item = match["item"]
        results.append({
            "type": item["type"],
            "name": item["name"],
            "path": item["path"],
            "score": match["score"]
        })

    return results

def open_file_or_folder(query):
    items = get_file_index()
    matches = find_matches(query, items)
    if not matches:
        return {
            "status": "not_found"
        }

    if len(matches) == 1:
        match = matches[0]["item"]

        subprocess.Popen(
            ["xdg-open", match["path"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return {
            "status": "opened",
            "item": match
        }

    best_score = matches[0]["score"]
    second_score = matches[1]["score"]

    # Clear winner
    if best_score - second_score >= 20:
        match = matches[0]["item"]

        subprocess.Popen(
            ["xdg-open", match["path"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return {
            "status": "opened",
            "item": match
        }

    # Ask user
    return {
        "status": "multiple_matches",
        "matches": [m["item"] for m in matches],
        "total_matches": len(matches)
    }