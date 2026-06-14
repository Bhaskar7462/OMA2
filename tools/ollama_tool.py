from ollama import chat
import time


def ask_llm(prompt):
    print("🤖 Thinking...")
    start_time = time.time()

    response = chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "system",
                "content": """
                You are a helpful assistant.
                Never show your reasoning.
                Never show your thinking process.
                Never show analysis.
                Respond directly with the final answer only.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False
    )

    end_time = time.time()
    print(
        f"\n⏱ Response time: "
        f"{end_time - start_time:.2f} seconds"
    )

    return response["message"]["content"]



# MEMORY PARSER LLM


def ask_llm_memory(prompt):

    response = chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "system",
                "content": """
You are a memory parser.

Your task is to classify the user's message into one of these intents:

SAVE
GET
DELETE
LIST
NONE

Return ONLY valid JSON.

Examples:

User:
Remember that my favorite editor is VS Code

Output:
{
    "intent":"SAVE",
    "key":"favorite editor",
    "value":"VS Code"
}

User:
What is my favorite editor

Output:
{
    "intent":"GET",
    "key":"favorite editor"
}

User:
Forget my favorite editor

Output:
{
    "intent":"DELETE",
    "key":"favorite editor"
}

User:
What do you know about me

Output:
{
    "intent":"LIST"
}

User:
Tell me a joke

Output:
{
    "intent":"NONE"
}
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False
    )

    return response["message"]["content"]