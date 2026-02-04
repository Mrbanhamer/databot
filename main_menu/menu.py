import os    # Goal: Standard Library 1 (System interaction)
import json  # Goal: Standard Library 2 (Data serialization)

def clear_screen():
    """Clears the terminal screen based on the OS."""
    # Functional Contribution: Cross-platform compatibility
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:                # For Mac and Linux
        os.system('clear')

def main_menu():
    # Goal: Advanced Data Type (Loading from a JSON string or file)
    # This replaces your hardcoded dict with a data-driven approach
    subreddits_json = '{"1": "python", "2": "technology", "3": "datascience"}'
    subreddits = json.loads(subreddits_json)

    while True:
        clear_screen()  # Use of 'os' to keep the menu clean
        print("=== Reddit Data Navigator ===")
        print("Current Directory:", os.getcwd()) # Shows your current folder path
        
        for key, name in subreddits.items():
            print(f"{key}. View r/{name}")
        
        exit_val = str(len(subreddits) + 1)
        print(f"{exit_val}. Exit")

        choice = input(f"\nSelect an option (1-{exit_val}): ")

        if choice in subreddits:
            print(f"\nNavigating to r/{subreddits[choice]}...")
            input("Press Enter to return to menu...") # Pause so user can see it
        elif choice == exit_val:
            print("Exiting... Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    main_menu()