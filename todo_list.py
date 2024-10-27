# Create an empty list to hold the tasks
task_list = []

# Function to add tasks
def add_task(task):
    task_list.append(task)
    print(f"Task added: {task}")

# Function to display tasks
def show_tasks():
    print("Task List:")
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")

# Function to delete tasks
def delete_task(index):
    try:
        deleted_task = task_list.pop(index - 1)
        print(f"Task deleted: {deleted_task}")
    except IndexError:
        print("Invalid task number.")

# Simple menu for user input
while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Make a choice: ")

    if choice == "1":
        new_task = input("New task: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        task_to_delete = int(input("Task number to delete: "))
        delete_task(task_to_delete)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
