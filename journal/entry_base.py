from datetime import datetime

class Entry:
    def __init__(self, username, entry_type):
        self.username = username
        self.entry_type = entry_type
        self.timestamp = datetime.now().strftime("%A, %d-%m-%Y %I:%M %p")

    def to_dict(self):
        return {
            "username": self.username,
            "type": self.entry_type,
            "timestamp": self.timestamp
        }