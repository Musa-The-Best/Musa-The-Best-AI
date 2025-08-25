import requests

def fetch_fact_from_url(url: str):
    """
    Fetches a random fact from a given URL and prints it.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fact_data = response.json()
            print(f"Did you know? {fact_data['text']}")
        else:
            print("Failed to retrieve fact.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main loop for user interaction. Prompts the user to select a category
    and fetches a random fact from that category.
    """
    print("Welcome to the Random Fact Fetcher!")
    print("Choose a category to fetch a random fact!")

    categories = {
        "1": "General Fact",
        "2": "Technology Fact",
        "3": "History Fact",
        "4": "Science Fact",
        "5": "Sports Fact",  # Example category, if you find a suitable endpoint
        "6": "Music Fact",   # Example category, if you find a suitable endpoint
    }

    # Process available categories to the user
    for key, category in categories.items():
        print(f"({key}) {category}")

    while True:
        category_choice = input("Enter the number corresponding to the category you want to explore (or 'q' to quit): ")
        if category_choice.lower() == "q":
            print("Goodbye!")
            break

        # Handle different categories
        if category_choice == "1":
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
        elif category_choice == "2":
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
        elif category_choice == "3":
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
        elif category_choice == "4":
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
        elif category_choice == "5":
            url = "https://uselessfacts.jsph.pl/random.json?language=en"  # Adjust this URL if endpoint is available
        elif category_choice == "6":
            url = "https://uselessfacts.jsph.pl/random.json?language=en"  # Adjust this URL if endpoint is available
        else:
            print("Invalid choice, please try again.")
            continue

        # Fetch and display the fact
        fetch_fact_from_url(url)

        # Ask if the user wants to continue
        continue_choice = input("Do you want to get another fact? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()