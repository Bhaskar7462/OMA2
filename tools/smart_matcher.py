import os
from rapidfuzz import fuzz


BAD_KEYWORDS = [
    "crashpad",
    "sandbox",
    "zygote",
    "renderer",
    "gpu",
    "utility"
]


def calculate_score(user_input, app):
    user_input = user_input.lower()
    process_name = app.get("process_name","").lower()
    exe_path = app.get("exe_path",""    ).lower()
    window_title = app.get("window_title","").lower()


    # Exact Match Shortcut

    exact_match_bonus = 0
    if user_input == process_name:
        exact_match_bonus = 50


    # Individual Scores


    name_score = fuzz.ratio(
        user_input,
        process_name
    )

    exe_name = os.path.basename(
        exe_path
    ).lower()

    path_score = fuzz.partial_ratio(
        user_input,
        exe_path
    )

    exe_score = fuzz.ratio(
        user_input,
        exe_name
    )


    title_score = fuzz.partial_ratio(
        user_input,
        window_title
    )


    # Weighted Score

    final_score = (
            name_score * 0.30
            + path_score * 0.10
            + exe_score * 0.20
            + title_score * 0.40
    )
    final_score += exact_match_bonus


    # Visible Window Bonus

    if window_title:
        final_score += 40


    # Title Contains Query


    if user_input in window_title:
        final_score += 20


    # Helper Process Penalty


    combined_text = (
        process_name
        + " "
        + exe_path
        + " "
        + window_title
    )

    for keyword in BAD_KEYWORDS:
        if keyword in combined_text:
            final_score -= 50
    return final_score


def find_best_match(
        user_input,
        candidates,
        threshold=70
):

    scored = []
    for app in candidates:
        score = calculate_score(
            user_input,
            app
        )

        scored.append(
            (score, app)
        )

    scored.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    top_matches = [
        item
        for item in scored
        if item[0] >= threshold
    ][:3]
    if not top_matches:
        return None, []

    best_score, best_app = top_matches[0]

    return best_app, top_matches