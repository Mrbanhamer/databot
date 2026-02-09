import os
import json
import sys

def main_menu():
    subreddits_json = '{"1": "python", "2": "technology", "3": "datascience"}'
    subreddits = json.loads(subreddits_json)

    while True:
        print("=== Reddit Data Navigator ===\n")
        print("Current Directory:", os.getcwd(), "\n")
        
        for key, name in subreddits.items():
            print(f"{key}. r/{name}")
        
        exit_val = str(len(subreddits) + 1)
        print(f"{exit_val}. Exit")
        
        choice = input(f"\nSelect an option (1-{exit_val}): ").strip()
        
        if choice in subreddits:
            selected_subreddit = subreddits[choice]
            print(f"\nYou selected r/{selected_subreddit}!")
            input("Press Enter to continue...")
            return selected_subreddit  # Return the string of the selected subreddit
        elif choice == exit_val:
            print("Exiting... Goodbye!")
            sys.exit()  # Immediately terminate the program
        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    result = main_menu()
    if result:
        print(f"Selected subreddit: {result}")
