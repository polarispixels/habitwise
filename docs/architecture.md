```mermaid
graph TD
  GUI[User Interface - Tkinter]
  GUI -->|Creates| Habit
  GUI -->|Marks Complete| Habit
  GUI --> Tracker
  Tracker --> JSON[habits.json]
  JSON -->|Loads| Tracker
  Tracker -->|Returns Habit List| GUI
```
