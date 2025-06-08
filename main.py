import os
from users.auth import login
from journal.journal_manager import JournalManager
from input.input_handlers import clear_screen, show_main_menu

def main():
    clear_screen()
    print("📝 Welcome to Reflective Journal CLI App!")
    user = login()

    if not user:
        print("Exiting app.")
        return

    manager = JournalManager(user)

    while True:
        choice = show_main_menu()

        if choice == "1":
            manager.start_entry_menu()
        elif choice == "2":
            manager.view_entries_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()