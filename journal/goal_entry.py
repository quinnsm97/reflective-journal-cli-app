from .entry_base import Entry

class GoalEntry(Entry):
    def __init__(self, username, goals_3mo, goals_1yr, goals_3yr):
        super().__init__(username, "Goal")
        self.goals_3mo = goals_3mo
        self.goals_1yr = goals_1yr
        self.goals_3yr = goals_3yr

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "3_month": self.goals_3mo,
            "1_year": self.goals_1yr,
            "3_year": self.goals_3yr
        })
        return base