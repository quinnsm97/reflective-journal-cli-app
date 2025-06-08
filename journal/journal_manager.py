import json
import os
from rich.prompt import Prompt
from rich.console import Console
from journal.feeling_entry import FeelingEntry
from journal.thought_entry import ThoughtEntry
from journal.goal_entry import GoalEntry
from journal.win_entry import WinEntry
from input.input_handlers import confirm_save, ask_to_continue, clear_screen

console = Console()
DATA_FILE = "data/journal_entries.json"

class JournalManager:
    def __init__(self, username):
        self.username = username
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def save_entry(self, entry):
        with open(DATA_FILE, "r+") as f:
            data = json.load(f)
            data.append(entry.to_dict())
            f.seek(0)
            json.dump(data, f, indent=2)

    def start_entry_menu(self):
        while True:
            clear_screen()
            console.print("[bold underline cyan]Start Journal Entry[/]")
            console.print("1. Feelings\n2. Irrational vs Rational Thought\n3. Goals\n4. Wins\n5. Back")
            choice = Prompt.ask("Select option", choices=["1", "2", "3", "4", "5"])

            if choice == "1":
                self.handle_feelings()
            elif choice == "2":
                self.handle_thoughts()
            elif choice == "3":
                self.handle_goals()
            elif choice == "4":
                self.handle_wins()
            elif choice == "5":
                break

    def handle_feelings(self):
        f = Prompt.ask("What are you feeling?")
        r = Prompt.ask("Why do you think you're feeling this?")
        i = Prompt.ask("How strong is it (1-10)?")
        ft = Prompt.ask("When do you first remember feeling this way?")
        entry = FeelingEntry(self.username, f, r, i, ft)

        if confirm_save(): self.save_entry(entry)
        if ask_to_continue(): self.handle_thoughts()

    def handle_thoughts(self):
        irr = Prompt.ask("Write your irrational thought/belief")
        rat = Prompt.ask("Now reframe it rationally")
        entry = ThoughtEntry(self.username, irr, rat)

        if confirm_save(): self.save_entry(entry)
        if ask_to_continue(): self.handle_goals()

    def handle_goals(self):
        g3 = Prompt.ask("What are your 3-month goals?")
        g1 = Prompt.ask("What are your 1-year goals?")
        g3y = Prompt.ask("What are your 3-year goals?")
        entry = GoalEntry(self.username, g3, g1, g3y)

        if confirm_save(): self.save_entry(entry)
        if ask_to_continue(): self.handle_wins()

    def handle_wins(self):
        while True:
            win = Prompt.ask("Enter a recent win")
            expand = Prompt.ask("Would you like to expand on it?", choices=["y", "n"])
            details = None
            if expand == "y":
                why = Prompt.ask("Why is this a win?")
                progress = Prompt.ask("How can you continue making progress?")
                next_step = Prompt.ask("What's your next step?")
                details = {"why": why, "progress": progress, "next_step": next_step}
            entry = WinEntry(self.username, win, details)
            if confirm_save(): self.save_entry(entry)

            another = Prompt.ask("Add another win?", choices=["y", "n"])
            if another == "n": break

    def view_entries_menu(self):
        clear_screen()
        console.print("[bold underline magenta]View Past Entries[/]")
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        user_entries = [e for e in data if e["username"] == self.username]
        if not user_entries:
            console.print("No entries found.")
            return

        console.print("1. View all\n2. By type\n3. Search by keyword\n4. Back")
        choice = Prompt.ask("Choose", choices=["1", "2", "3", "4"])

        if choice == "1":
            for e in user_entries:
                console.print(e)
        elif choice == "2":
            t = Prompt.ask("Which type? (Feeling, Thought, Goal, Win)")
            for e in user_entries:
                if e["type"].lower() == t.lower():
                    console.print(e)
        elif choice == "3":
            keyword = Prompt.ask("Enter keyword")
            for e in user_entries:
                if keyword.lower() in str(e).lower():
                    console.print(e)