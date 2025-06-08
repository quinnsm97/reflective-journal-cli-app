from .entry_base import Entry

class ThoughtEntry(Entry):
    def __init__(self, username, irrational, rational):
        super().__init__(username, "Thought")
        self.irrational = irrational
        self.rational = rational

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "irrational": self.irrational,
            "rational": self.rational
        })
        return base