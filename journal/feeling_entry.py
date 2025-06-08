from .entry_base import Entry

class FeelingEntry(Entry):
    def __init__(self, username, feeling, reason, intensity, first_time):
        super().__init__(username, "Feeling")
        self.feeling = feeling
        self.reason = reason
        self.intensity = intensity
        self.first_time = first_time

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "feeling": self.feeling,
            "reason": self.reason,
            "intensity": self.intensity,
            "first_time": self.first_time
        })
        return base