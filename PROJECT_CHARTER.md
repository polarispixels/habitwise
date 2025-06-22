# 📘 Project Charter: HabitWise (Habit Tracker with GUI)

## 1. Project Purpose / Problem Statement
Many people want to build better habits but lack a lightweight, distraction-free tool to track their progress. Most tools are bloated, require sign-ins, or overwhelm users with features. We aim to create a minimal, personal-use habit tracker that is easy to use, customizable, and built using Python with a simple GUI.

## 2. Goals and Objectives
- Build a local desktop application to track daily habits
- Provide a clean and intuitive GUI (Tkinter to start)
- Allow users to:
  - Add and edit habits
  - Mark habits as done for the day
  - View history/progress for each habit
- Persist data locally (using JSON or SQLite)

## 3. Scope
**In Scope:**
- Cross-platform Python GUI using Tkinter  
- Daily checklist view  
- Simple analytics (streaks, completion rate)  
- Local storage only  

**Out of Scope:**
- Syncing across devices  
- User accounts  
- Notifications or reminders  

## 4. Deliverables
- A working Python GUI app (Tkinter-based)
- `README.md` with setup instructions
- Optional: Export/import habit data (JSON)

## 5. Timeline / Milestones

| Phase                      | Target Completion |
|---------------------------|-------------------|
| Project Setup             | Day 1             |
| Basic GUI + Add Habits    | Day 2             |
| Mark/Track Habits         | Day 3             |
| Store Data Persistently   | Day 4             |
| Add Analytics View        | Day 5             |
| Polish and Package        | Day 6             |

---

## ✅ User Acceptance Criteria (UAC)

| ID    | Acceptance Criteria                                                      | Priority    |
|-------|---------------------------------------------------------------------------|-------------|
| UAC-1 | User can launch the app and see today’s habit list                       | Must Have   |
| UAC-2 | User can add a new habit and see it appear instantly                     | Must Have   |
| UAC-3 | User can mark a habit as complete for the day                            | Must Have   |
| UAC-4 | User can see a history of completed days for each habit                  | Should Have |
| UAC-5 | User’s data persists after closing and reopening the app                 | Must Have   |
| UAC-6 | App loads in under 2 seconds and uses minimal system resources           | Should Have |
| UAC-7 | App does not crash when given invalid input (e.g., empty habit name)     | Must Have   |
| UAC-8 | User can delete a habit with confirmation                                | Could Have  |

---

## 📎 Version
Charter v1.0 – Created June 22, 2025

