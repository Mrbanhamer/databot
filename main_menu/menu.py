import json
import os

def load_reddit_data(subreddit):
    filename = f"{subreddit}.json"
    
    # Check if the file exists before trying to open it
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            print(f"\n--- Data for r/{subreddit} ---")
            # Just printing the first entry as an example
            print(data[0] if data else "File is empty.")
    else:
        print(f"\nError: No data found for {subreddit}. Run the scraper first!")

def main_menu():
    while True:
        print("\n=== Reddit Data Navigator ===")
        print("1. View r/Python")
        print("2. View r/Technology")
        print("3. View r/DataScience")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            load_reddit_data("python")
        elif choice == '2':
            load_reddit_data("technology")
        elif choice == '3':
            load_reddit_data("datascience")
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()