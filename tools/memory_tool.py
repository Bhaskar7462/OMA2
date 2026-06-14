import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MEMORY_FILE = os.path.join(BASE_DIR,
    "data",
    "memory.json"
)


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(
            MEMORY_FILE,
            "r"
        ) as file:
            return json.load(file)

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):
        return {}


def save_memory(key, value):

    memories = load_memory()

    memories[key] = value

    with open(
        MEMORY_FILE,
        "w"
    ) as file:
        json.dump(
            memories,
            file,
            indent=4
        )

    return True


def get_memory(key):

    memories = load_memory()

    return memories.get(key)


def get_all_memories():

    return load_memory()


def delete_memory(key):

    memories = load_memory()

    if key not in memories:
        return False

    del memories[key]

    with open(
        MEMORY_FILE,
        "w"
    ) as file:
        json.dump(
            memories,
            file,
            indent=4
        )

    return True