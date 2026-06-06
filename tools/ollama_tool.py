from ollama import chat
import time

def ask_llm(prompt):
    print("🤖 Thinking...")
    start_time = time.time()

    response = chat(
        model = "qwen3.5:4b",
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
    print(f"\n⏱ Response time: {end_time - start_time:.2f} seconds")
    return response["message"]["content"]
