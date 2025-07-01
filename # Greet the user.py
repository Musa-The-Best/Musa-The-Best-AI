# Greet the user
print("Hello! I am AI Bot. What's your name?")
name = input()

# Respond to the user's name
print(f"Nice to meet you, {name}!")

# Start a loop to keep the conversation going
while True:
    # Ask how the user is feeling
    print("How are you feeling today? (good/bad/okay)")
    mood = input().lower()

    # Respond based on the mood
    if mood == "good":
        print("I'm glad to hear that! What made your day good?")
    elif mood == "bad":
        print("I'm sorry to hear that. Is there something you want to share?")
    elif mood == "okay":
        print("Got it. Sometimes 'okay' is just right.")
    else:
        print("I see. Sometimes it's hard to put feelings into words.")

    # Follow-up question for more interaction
    print("What is one thing you like to do in your free time?")
    hobby = input()
    print(f"That sounds fun! {hobby} is a great way to spend time.")

    # Ask if the user wants to continue
    print("Would you like to keep chatting? (yes/exit)")
    choice = input().lower()

    # Check if the user wants to exit the chat
    if choice == "exit":
        print(f"It was nice chatting with you, {name}. Goodbye!")
        break
