import re
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Memory for previous input
user_memory = {}

# Simulated features
def get_weather():
    return "It's sunny with a temperature of 25°C."

def get_news():
    return "Today's news: ChatGPT helps students learn Python."

def get_local_time(city="New York"):
    return f"The local time in {city} is {time.strftime('%H:%M:%S')}."

# Input handler
def handle_input(user_input):
    # Store the last input
    user_memory["last_input"] = user_input

    # Normalize input
    user_input = user_input.lower()

    # Patterns and keyword handling
    if re.search(r"weather|temperature|forecast", user_input):
        return Fore.CYAN + get_weather()

    elif re.search(r"news|headline|update", user_input):
        return Fore.YELLOW + get_news()

    elif re.search(r"time.*\b(in|at)?\s*(\w+)?", user_input):
        match = re.search(r"time.*\b(in|at)?\s*(\w+)?", user_input)
        city = match.group(2) if match and match.group(2) else "New York"
        return Fore.MAGENTA + get_local_time(city)

    elif "memory" in user_input:
        last = user_memory.get("last_input", "No previous input found.")
        return Fore.GREEN + f"Last input: {last}"

    elif "hello" in user_input or "hi" in user_input:
        return Fore.BLUE + "Hello! How can I help you today?"

    elif "bye" in user_input:
        return Fore.RED + "Goodbye!"

    else:
        # Placeholder for future NLP handling
        return Style.DIM + "I'm not sure I understand. Can you rephrase?"

# Main loop
def chatbot():
    print(Fore.GREEN + "Welcome to the Enhanced Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input(Fore.WHITE + "You: ")
        response = handle_input(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chatbot()
