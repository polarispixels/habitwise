from datetime import date, timedelta
from typing import List

class Habit:
    def __init__(self, name: str, created=None, completed_dates=None):
        from datetime import date
        self.name = name
        self.created = created or date.today().isoformat()
        self.completed_dates = completed_dates or []

    def mark_completed_today(self):
        from datetime import date
        today_str = date.today().isoformat()
        if today_str not in self.completed_dates:
            self.completed_dates.append(today_str)

    def is_completed_today(self) -> bool:
        from datetime import date
        return date.today().isoformat() in self.completed_dates

    def __repr__(self):
        return f"<Habit name='{self.name}' completed_today={self.is_completed_today()}>"
    
    def get_streak(self) -> int:
        if not self.completed_dates:
            return 0

        completed = set(self.completed_dates)
        streak = 0
        current_day = date.today()

        while current_day.isoformat() in completed:
            streak += 1
            current_day -= timedelta(days=1)

        return streak
