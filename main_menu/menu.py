import json
import os

def main_menu():
    while True:
        print("\n=== Reddit Data Navigator ===")
        print("1. View r/Python")
        print("2. View r/Technology")
        print("3. View r/DataScience")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            return "python"
        elif choice == '2':
            return "technology"
        elif choice == '3':
            return "datascience"
        elif choice == '4':
            print("Exiting... Goodbye!")
            return 'None'
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()