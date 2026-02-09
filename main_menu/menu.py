import os
import json
import sys
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def main_menu():
    subreddits_json = '{"1": "python", "2": "technology", "3": "datascience"}'
    subreddits = json.loads(subreddits_json)

    while True:
        print(Fore.CYAN + "Welcome to The Reddit DataBot!")
        print(Fore.LIGHTMAGENTA_EX + "=== Reddit Data Navigator ===\n" + Style.RESET_ALL)
        print(Fore.WHITE + "Current Directory: " + Fore.YELLOW + os.getcwd() + "\n")

        for key, name in subreddits.items():
            print(Fore.GREEN + f"{key}." + Fore.WHITE + f" r/{name}")

        custom_option = str(len(subreddits) + 1)
        exit_val = str(len(subreddits) + 2)

        print(Fore.MAGENTA + f"{custom_option}. Enter custom subreddit")
        print(Fore.RED + f"{exit_val}. Exit")

        choice = input(Fore.CYAN + f"\nSelect an option (1-{exit_val}): " + Style.RESET_ALL).strip()

        if choice in subreddits:
            selected_subreddit = subreddits[choice]
            print(Fore.GREEN + f"\nYou selected r/{selected_subreddit}!")
            input(Fore.YELLOW + "Press Enter to continue...")
            return selected_subreddit
<<<<<<< HEAD
        elif choice == exit_val:
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()  
=======

        elif choice == custom_option:
            custom = input(Fore.CYAN + "\nEnter subreddit name (without r/): " + Style.RESET_ALL).strip()

            # Enkel validering: ta bort ev. "r/" och trimma
            custom = custom.replace("r/", "").strip().lower()

            if custom and " " not in custom:
                print(Fore.GREEN + f"\nYou selected r/{custom}!")
                input(Fore.YELLOW + "Press Enter to continue...")
                return custom
            else:
                input(Fore.RED + "Invalid subreddit name. Press Enter to try again...")

        elif choice == exit_val:
            print(Fore.RED + "\nExiting... Goodbye!")
            sys.exit()

>>>>>>> 81b440a1e56b8e6b77ae808e4568f4c4060f34e0
        else:
            input(Fore.RED + "Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    result = main_menu()
    if result:
        print(Fore.LIGHTGREEN_EX + f"\nSelected subreddit: {result}")
