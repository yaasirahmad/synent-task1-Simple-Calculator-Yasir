"""
Task Manager - Menu-Driven CLI Program
Student ID: F20243798
"""

tasks = []

def display_menu():
    print("\n" + "="*40)
    print("       TASK MANAGER")
    print("="*40)
    print("  1. View Tasks")
    print("  2. Add Task")
    print("  3. Delete Task")
    print("  4. Exit")
    print("="*40)

def view_tasks():
    print("\n--- YOUR TASKS ---")
    if not tasks:
        print("  No tasks yet. Add one to get started!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"  [{i}] {task}")
    print()

def add_task():
    task = input("Enter task description: ").strip()
    if task:
        tasks.append(task)
        print(f"  ✓ Task added: '{task}'")
    else:
        print("  ✗ Task cannot be empty.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"  ✓ Deleted: '{removed}'")
        else:
            print("  ✗ Invalid task number.")
    except ValueError:
        print("  ✗ Please enter a valid number.")

def main():
    print("\nWelcome to Task Manager!")
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\nGoodbye! Stay productive.\n")
            break
        else:
            print("  ✗ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()