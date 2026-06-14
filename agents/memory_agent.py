from tools.memory_parser_tool import (
    parse_memory_intent
)

from tools.memory_tool import (
    save_memory,
    get_memory,
    get_all_memories,
    delete_memory
)


def memory_agent(user_input):

    result = parse_memory_intent(
        user_input
    )

    intent = result.get(
        "intent",
        "NONE"
    )

    # SAVE

    if intent == "SAVE":

        key = result.get(
            "key"
        )

        value = result.get(
            "value"
        )

        if not key or not value:
            return (
                "I couldn't understand "
                "what to remember."
            )

        old_value = get_memory(
            key
        )

        save_memory(
            key,
            value
        )

        if old_value is None:
            return (
                f"Okay, I'll remember "
                f"that your {key} "
                f"is {value}."
            )

        return (
            f"Updated memory:\n"
            f"{key}: "
            f"{old_value} → {value}"
        )

    # GET

    if intent == "GET":

        key = result.get(
            "key"
        )

        if not key:
            return (
                "I couldn't understand "
                "which memory to retrieve."
            )

        value = get_memory(
            key
        )

        if value is None:
            return (
                f"I don't know your "
                f"{key} yet."
            )

        return (
            f"Your {key} "
            f"is {value}."
        )

    # DELETE

    if intent == "DELETE":

        key = result.get(
            "key"
        )

        if not key:
            return (
                "I couldn't understand "
                "which memory to delete."
            )

        deleted = delete_memory(
            key
        )

        if deleted:
            return (
                f"I forgot your "
                f"{key}."
            )

        return (
            f"I don't have any "
            f"memory for {key}."
        )

    # LIST

    if intent == "LIST":

        memories = get_all_memories()

        if not memories:
            return (
                "I don't know anything "
                "about you yet."
            )

        output = []

        for key, value in memories.items():

            output.append(
                f"{key}: {value}"
            )

        return "\n".join(
            output
        )
    # NONE
    return None