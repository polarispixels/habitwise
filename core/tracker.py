import json
from pathlib import Path
from core.habit import Habit
from typing import List

DATA_FILE = Path("data/habits.json")

def save_habits(habits: List[Habit]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([habit.__dict__ for habit in habits], f, indent=2)

def load_habits() -> List[Habit]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        return [Habit(**habit) for habit in raw_data]
