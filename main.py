"""
Synent Technologies - Python Development Internship
Task 3: To-Do List Application (CLI)
"""

import json
import os
import sys

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as err:
        print(f"\n[Error] Could not save tasks: {err}")


def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n" + "=" * 45)
    print(f"{'#':<4} {'Status':<8} {'Task Description'}")
    print("-" * 45)
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task.get("completed") else "[ ]"
        print(f"{index:<4} {status:<8} {task.get('title', '')}")
    print("=" * 45)


def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if not title:
        print("[Error] Task description cannot be empty.")
        return
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"[Success] Added: '{title}'")


def mark_task_complete(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter task number to toggle status: "))
        if 1 <= choice <= len(tasks):
            task = tasks[choice - 1]
            task["completed"] = not task["completed"]
            save_tasks(tasks)
            state = "Completed" if task["completed"] else "Pending"
            print(f"[Success] Task #{choice} set to {state}.")
        else:
            print("[Error] Invalid task number.")
    except ValueError:
        print("[Error] Please enter a valid number.")


def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"[Success] Deleted: '{removed.get('title')}'")
        else:
            print("[Error] Invalid task number.")
    except ValueError:
        print("[Error] Please enter a valid number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Toggle Task Complete / Pending")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nExiting program. Goodbye!\n")
            sys.exit(0)
        else:
            print("[Error] Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()