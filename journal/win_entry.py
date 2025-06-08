from .entry_base import Entry

class WinEntry(Entry):
    def __init__(self, username, win, details=None):
        super().__init__(username, "Win")
        self.win = win
        self.details = details

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "win": self.win,
            "details": self.details
        })
        return base