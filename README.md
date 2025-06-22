# 🌱 HabitWise – A Minimal Habit Tracker

Track your habits every day with a distraction-free, local-first app designed for focus, not friction.

> “Sow a thought and you reap an action; sow an act and you reap a habit; sow a habit and you reap a character; sow a character and you reap a destiny.” 
> — *Ralph Waldo Emerson*

---

## 📘 Project Overview

HabitWise is a lightweight desktop habit tracker built with Python and Tkinter. It allows users to:

- ✅ Create and track daily habits
- ✅ Mark them complete with a simple GUI
- ✅ View dynamic streaks
- ✅ Persist data locally (no sign-in, no cloud sync)

See the [📄 PROJECT_CHARTER.md](./PROJECT_CHARTER.md) for detailed goals, scope, and versioning milestones.

## 📂 Documentation

- [Architecture Diagram](docs/architecture.md)
- [Component Map](docs/components.md)
- [User Journey](docs/user-journey.md)
- [State Machine](docs/state-machine.md)
- [Feature Roadmap](docs/roadmap.md)

---

## 🧑‍💻 Developer Setup

### ✅ Prerequisites

- Python 3.10+
- `pip`, `venv` (included with Python)
- Git
- (Optional) WSL for a full Linux environment on Windows

### 🚀 Install & Run (for Development)

```bash
git clone https://github.com/your-username/habitwise.git
cd habitwise
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt  # If requirements.txt is used
python main.py
```

### 🔎 Run Tests

```bash
python -m unittest discover tests
```

> ✅ Pre-commit hook included: unit tests run automatically before every commit

---

## 📦 Publishing the App

### Build a Windows Executable (via PyInstaller)

> Make sure virtual environment is activated

```bash
pip install pyinstaller
pyinstaller main.py --onefile --windowed --name HabitWise
```

Your `.exe` will appear in the `dist/` folder:

```
habitwise/
├── dist/
│   └── HabitWise.exe  ← ✅ Run this
```

### Optional: Add Icon

```bash
pyinstaller main.py --onefile --windowed --name HabitWise --icon=assets/icon.ico
```

---

## 🧑‍🏫 How to Use (End User)

1. Launch `HabitWise.exe`
2. Add your daily habits via the input field
3. Use checkboxes to mark them done
4. View streaks in real time
5. Exit anytime — your progress is saved in `data/habits.json`

---

## 🧭 Roadmap

See the [📘 Project Charter](./PROJECT_CHARTER.md) for full scope, UAC, and milestones.

Planned enhancements for v1.1:
- Habit streak visualization
- Improved input validation
- Data export/import
- Optional cloud sync (out of scope for v1.0)

---

## 📜 License

MIT License (optional — add if open-sourcing).

---

## 💬 Attribution

> “Sow a thought and you reap an action; sow an act and you reap a habit; sow a habit and you reap a character; sow a character and you reap a destiny.” 
> — *Ralph Waldo Emerson*
