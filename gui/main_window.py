import tkinter as tk
from tkinter import ttk
from core.tracker import load_habits, save_habits
from core.habit import Habit

def run_gui():
    habits = load_habits()

    def toggle_habit(habit: Habit, var: tk.BooleanVar):
        if var.get():
            habit.mark_completed_today()
        else:
            if habit.is_completed_today():
                habit.completed_dates.remove(habit.created)
        save_habits(habits)

    def refresh_habit_list():
        for widget in habit_frame.winfo_children():
            widget.destroy()

        for habit in habits:
            row = ttk.Frame(habit_frame)
            row.pack(fill="x", pady=3, padx=10)

            var = tk.BooleanVar(value=habit.is_completed_today())
            cb = ttk.Checkbutton(
                row,
                text=f"{habit.name} ({habit.get_streak()}🔥)",
                variable=var,
                command=lambda h=habit, v=var: toggle_habit(h, v)
            )
            cb.pack(side="left", expand=True, anchor="w")

            del_button = ttk.Button(
                row,
                text="🗑",
                width=2,
                command=lambda h=habit: delete_habit(h)
            )
            del_button.pack(side="right")


    def add_habit():
        name = new_habit_var.get().strip()
        if name and not any(h.name == name for h in habits):
            habit = Habit(name)
            habits.append(habit)
            save_habits(habits)
            new_habit_var.set("")
            refresh_habit_list()

    def delete_habit(habit_to_remove: Habit):
        habits.remove(habit_to_remove)
        save_habits(habits)
        refresh_habit_list()


    root = tk.Tk()
    root.title("HabitWise")
    root.geometry("300x450")

    ttk.Label(root, text="Today's Habits", font=("Arial", 16)).pack(pady=10)

    habit_frame = ttk.Frame(root)
    habit_frame.pack(fill="both", expand=True)

    refresh_habit_list()

    # New habit input
    new_habit_var = tk.StringVar()
    entry = ttk.Entry(root, textvariable=new_habit_var)
    entry.pack(fill="x", padx=10, pady=(10, 0))

    add_button = ttk.Button(root, text="Add Habit", command=add_habit)
    add_button.pack(pady=5)

    root.mainloop()
