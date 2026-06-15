# it is responsible for opening application and file and folder

import subprocess

from tools.app_tool import find_apps
from tools.file_folder_opening_tool import find_files_and_folders


all_matches = []
current_page = 0


def open_selected_result(result):

    if result["type"] == "application":

        try:
            subprocess.Popen(
                ["gtk-launch", result["desktop_id"]],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            return f"Opening {result['name']}..."

        except Exception as e:
            return f"Error: {e}"

    try:
        subprocess.Popen(
            ["xdg-open", result["path"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return f"Opening {result['name']}..."

    except Exception as e:
        return f"Error: {e}"


def open_agent(user_input):
    global all_matches
    global current_page

    user_input = user_input.strip()


    # MORE

    if user_input.lower() == "more" and all_matches:

        current_page += 1

        start = current_page * 10
        end = start + 10

        page_matches = all_matches[start:end]

        if not page_matches:
            return "No more matches available."

        response = "More matches:\n\n"

        for i, match in enumerate(page_matches, start=start + 1):

            response += (
                f"{i}. "
                f"{match['name']} "
                f"({match['type']})\n"
            )

        response += (
            "\nType:\n"
            "- a number to open\n"
            '- "more" to continue'
        )

        return response


    # NUMBER SELECTION

    if all_matches and user_input.isdigit():

        choice = int(user_input)

        if 1 <= choice <= len(all_matches):

            selected = all_matches[choice - 1]

            result = open_selected_result(selected)

            all_matches = []
            current_page = 0

            return result

        return (
            f"Please choose a number "
            f"between 1 and {len(all_matches)}."
        )


    # NEW SEARCH

    query = (
        user_input.lower()
        .replace("open", "")
        .strip()
    )

    app_matches = find_apps(query)

    file_matches = find_files_and_folders(query)

    all_results = app_matches + file_matches

    if not all_results:
        return f"Sorry Boss, I couldn't find '{query}'."

    all_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Only one result exists
    if len(all_results) == 1:
        return open_selected_result(all_results[0])

    # Multiple results -> ALWAYS ask user
    all_matches = all_results
    current_page = 0

    response = f"I found {len(all_results)} matches.\n\n"

    response += "Top matches:\n\n"

    first_page = all_matches[:10]

    for i, match in enumerate(first_page, start=1):

        response += (
            f"{i}. "
            f"{match['name']} "
            f"({match['type']})\n"
        )

    response += (
        "\nType:\n"
        "- a number to open\n"
        '- "more" to see additional matches'
    )

    return response