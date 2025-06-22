import unittest
from datetime import date, timedelta
from core.habit import Habit

class TestHabit(unittest.TestCase):

    def test_create_habit(self):
        habit = Habit("Read")
        self.assertEqual(habit.name, "Read")
        self.assertIsInstance(habit.created, str)
        self.assertEqual(habit.completed_dates, [])

    def test_mark_completed_today(self):
        habit = Habit("Stretch")
        today = date.today().isoformat()
        habit.mark_completed_today()
        self.assertIn(today, habit.completed_dates)
        # Calling it again shouldn't add a duplicate
        habit.mark_completed_today()
        self.assertEqual(habit.completed_dates.count(today), 1)

    def test_is_completed_today(self):
        habit = Habit("Meditate")
        self.assertFalse(habit.is_completed_today())
        habit.mark_completed_today()
        self.assertTrue(habit.is_completed_today())

    def test_streak_logic(self):
        habit = Habit("Exercise")
        today = date.today()
        # Simulate completion on today, yesterday, day before yesterday
        habit.completed_dates = [
            (today - timedelta(days=0)).isoformat(),
            (today - timedelta(days=1)).isoformat(),
            (today - timedelta(days=2)).isoformat(),
        ]
        self.assertEqual(habit.get_streak(), 3)

        # Break the streak
        habit.completed_dates.remove((today - timedelta(days=1)).isoformat())
        self.assertEqual(habit.get_streak(), 1)

if __name__ == '__main__':
    unittest.main()
