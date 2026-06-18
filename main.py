from agents.coordinator_agent import coordinator_agent

print("...AI Assistant Started...")
print("...Type 'exit' to exit...\n")

while True:

    user_input = input("Boss > ")

    if user_input.lower() == "exit":
        print("Har Har Mahadev!! Boss")
        break

    response = coordinator_agent(user_input)

    print("\nAssistant > ")
    print(response)
    print()