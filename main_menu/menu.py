import os  # Standard Library for interacting with the operating system

def main_menu():
    # 1. ADVANCED DATA TYPES: Using a list to store dynamic data
    # We look for all files ending in .json and strip the extension
    data_folder = "./databot" # Assuming your JSONs are in a folder named 'data'
    
    # Ensure folder exists to avoid errors
    if not os.path.exists(data_folder):
        print(f"Error: {data_folder} folder not found.")
        return None

    # Use of list comprehension: scans directory and filters for .json files
    available_subreddits = [f.replace('.json', '') for f in os.listdir(data_folder) if f.endswith('.json')]

    # 2. CONDITIONS: Handle the case where no data has been collected yet
    if not available_subreddits:
        print("No data files found. Please run the bot first!")
        return None

    while True:
        print("\n=== Reddit Data Navigator ===")
        
        # 3. LOOPS: Dynamically generate the menu based on found files
        for index, name in enumerate(available_subreddits, start=1):
            print(f"{index}. View r/{name}")
        
        exit_option = len(available_subreddits) + 1
        print(f"{exit_option}. Exit")

        # 4. VARIABLES: Storing user input
        choice = input(f"\nSelect an option (1-{exit_option}): ")

        # 5. CONDITIONS & LOGIC: Validating the input
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(available_subreddits):
                return available_subreddits[idx]
            elif int(choice) == exit_option:
                print("Exiting... Goodbye!")
                return 'None'
        
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    selected = main_menu()
    if selected:
        print(f"Successfully selected: {selected}")