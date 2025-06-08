from rich.prompt import Prompt
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirm_save():
    return Prompt.ask("Save this entry?", choices=["y", "n"]) == "y"

def ask_to_continue():
    return Prompt.ask("Continue to next entry?", choices=["y", "n"]) == "y"

def show_main_menu():
    print("\nMain Menu:")
    print("1. Start Journal Entry")
    print("2. View Past Entries")
    print("3. Exit")
    return Prompt.ask("Choose option", choices=["1", "2", "3"])