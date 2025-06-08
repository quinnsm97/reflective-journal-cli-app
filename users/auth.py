import bcrypt
import json
import os
from rich.prompt import Prompt
from rich.console import Console

USER_FILE = "data/users.json"
console = Console()

def login():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)

    with open(USER_FILE, "r") as f:
        users = json.load(f)

    choice = Prompt.ask("Login or Register?", choices=["login", "register"])

    username = Prompt.ask("Username")
    password = Prompt.ask("Password", password=True)

    if choice == "register":
        if username in users:
            console.print("User already exists.")
            return None
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        users[username] = hashed
        with open(USER_FILE, "w") as f:
            json.dump(users, f)
        console.print("Registration successful!")
        return username

    elif choice == "login":
        if username not in users:
            console.print("User does not exist.")
            return None
        if bcrypt.checkpw(password.encode(), users[username].encode()):
            console.print(f"Welcome back, {username}!")
            return username
        else:
            console.print("Incorrect password.")
            return None