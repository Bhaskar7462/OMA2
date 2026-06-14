# it is responsible for doing
# Natural Language ---> Intent JSON

import json

from tools.ollama_tool import (
    ask_llm_memory
)


def parse_memory_intent(user_input):

    response = ask_llm_memory(
        user_input
    )

    try:
        return json.loads(
            response
        )

    except json.JSONDecodeError:

        return {
            "intent": "NONE"
        }