import os
def calculate_score(query, item):
    score = 0

    name = item["name"].lower()
    query = query.lower().strip()

    # Exact filename match
    if name == query:
        score += 100

    # Exact stem match
    stem = os.path.splitext(name)[0]

    if stem == query:
        score += 200

    elif name.startswith(query):
        score += 80

    elif query in name:
        score += 60

    else:
        return None

    # Folder bonus
    if item["type"] == "folder":
        score += 10

    # Prefer shorter names
    score += max(0, 20 - len(name))

    # File type bonus
    if name.endswith(".pdf"):
        score += 10

    elif name.endswith(".docx"):
        score += 5

    # Penalties
    penalties = [
        "(1)",
        "(2)",
        "copy",
        "backup",
        "old",
        "temp",
        ".bak",
        "high_fidelity",
        "fixed_links"
    ]

    for penalty in penalties:
        if penalty in name:
            score -= 15

    return score


def find_matches(query, items):
    scored_matches = []
    for item in items:
        score = calculate_score(query, item)
        if score is None:
            continue
        scored_matches.append({
            "score": score,
            "item": item
        })

    scored_matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_matches