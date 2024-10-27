import datetime
import json

# Görev listesini tutmak için boş bir liste oluştur
task_list = []

# Görevleri eklemek için fonksiyon
def add_task(task, due_date, category, priority):
    task_list.append({'task': task, 'due_date': due_date, 'category': category, 'priority': priority, 'completed': False, 'completion_date': None})
    print(f"Task added: {task} - Due: {due_date} - Category: {category} - Priority: {priority}")

# Görevleri görüntülemek için fonksiyon
def show_tasks():
    print("Task List:")
    for i, task_info in enumerate(task_list, 1):
        status = "Completed" if task_info['completed'] else "Incomplete"
        completion_date = task_info['completion_date'] if task_info['completion_date'] else "N/A"
        print(f"{i}. {task_info['task']} - Due: {task_info['due_date']} - Category: {task_info['category']} - Priority: {task_info['priority']} - Status: {status} - Completion Date: {completion_date}")

# Görevleri silmek için fonksiyon
def delete_task(index):
    try:
        deleted_task = task_list.pop(index - 1)
        print(f"Task deleted: {deleted_task['task']}")
    except IndexError:
        print("Invalid task number.")

# Görevleri tamamlamak için fonksiyon
def complete_task(index):
    try:
        task_list[index - 1]['completed'] = True
        task_list[index - 1]['completion_date'] = datetime.date.today().strftime("%Y-%m-%d")
        print(f"Task completed: {task_list[index - 1]['task']}")
    except IndexError:
        print("Invalid task number.")

# Görevleri düzenlemek için fonksiyon
def edit_task(index, new_task, new_due_date):
    try:
        task_list[index - 1]['task'] = new_task
        task_list[index - 1]['due_date'] = new_due_date
        print(f"Task updated: {new_task} - Due: {new_due_date}")
    except IndexError:
        print("Invalid task number.")

# Tamamlanmış görevleri temizlemek için fonksiyon
def clear_completed_tasks():
    global task_list
    task_list = [task for task in task_list if not task['completed']]
    print("Completed tasks cleared.")

# Görevleri dosyaya kaydetmek için fonksiyon
def save_tasks(filename):
    with open(filename, 'w') as file:
        json.dump(task_list, file)
    print("Tasks saved.")

# Dosyadan görevleri yüklemek için fonksiyon
def load_tasks(filename):
    global task_list
    try:
        with open(filename, 'r') as file:
            task_list = json.load(file)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

# Kullanıcıdan giriş almak için basit bir menü
while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Edit Task")
    print("6. Clear Completed Tasks")
    print("7. Save Tasks")
    print("8. Load Tasks")
    print("9. Exit")
    choice = input("Make a choice: ")

    if choice == "1":
        new_task = input("New task: ")
        due_date = input("Due date (YYYY-MM-DD): ")
        category = input("Category: ")
        priority = input("Priority (High/Medium/Low): ")
        add_task(new_task, due_date, category, priority)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        task_to_delete = int(input("Task number to delete: "))
        delete_task(task_to_delete)
    elif choice == "4":
        show_tasks()
        task_to_complete = int(input("Task number to complete: "))
        complete_task(task_to_complete)
    elif choice == "5":
        show_tasks()
        task_to_edit = int(input("Task number to edit: "))
        new_task = input("New task description: ")
        new_due_date = input("New due date (YYYY-MM-DD): ")
        edit_task(task_to_edit, new_task, new_due_date)
    elif choice == "6":
        clear_completed_tasks()
    elif choice == "7":
        filename = input("Enter filename to save tasks: ")
        save_tasks(filename)
    elif choice == "8":
        filename = input("Enter filename to load tasks: ")
        load_tasks(filename)
    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
