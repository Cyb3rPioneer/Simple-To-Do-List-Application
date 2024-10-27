import tkinter as tk
from tkinter import messagebox
import datetime
import json

# Görev listesini tutmak için boş bir liste oluştur
task_list = []

# Görevleri eklemek için fonksiyon
def add_task():
    task = entry_task.get()
    due_date = entry_date.get()
    category = entry_category.get()
    priority = entry_priority.get()
    task_list.append({'task': task, 'due_date': due_date, 'category': category, 'priority': priority, 'completed': False, 'completion_date': None})
    listbox_tasks.insert(tk.END, f"{task} - {due_date} - {category} - {priority}")
    entry_task.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_priority.delete(0, tk.END)

# Görevleri silmek için fonksiyon
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        del task_list[selected_task_index]
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

# Görevleri tamamlamak için fonksiyon
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task_list[selected_task_index]['completed'] = True
        task_list[selected_task_index]['completion_date'] = datetime.date.today().strftime("%Y-%m-%d")
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"{task_list[selected_task_index]['task']} - {task_list[selected_task_index]['due_date']} - {task_list[selected_task_index]['category']} - {task_list[selected_task_index]['priority']} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

# Görevleri dosyaya kaydetmek için fonksiyon
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(task_list, file)
    messagebox.showinfo("Info", "Tasks saved")

# Dosyadan görevleri yüklemek için fonksiyon
def load_tasks():
    global task_list
    try:
        with open('tasks.json', 'r') as file:
            task_list = json.load(file)
        listbox_tasks.delete(0, tk.END)
        for task in task_list:
            listbox_tasks.insert(tk.END, f"{task['task']} - {task['due_date']} - {task['category']} - {task['priority']}")
        messagebox.showinfo("Info", "Tasks loaded")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found")

# GUI Uygulaması
root = tk.Tk()
root.title("To-Do List Application")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=70)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=70)
entry_task.pack()
entry_date = tk.Entry(root, width=70)
entry_date.pack()
entry_category = tk.Entry(root, width=70)
entry_category.pack()
entry_priority = tk.Entry(root, width=70)
entry_priority.pack()

button_add_task = tk.Button(root, text="Add Task", width=68, command=add_task)
button_add_task.pack()
button_delete_task = tk.Button(root, text="Delete Task", width=68, command=delete_task)
button_delete_task.pack()
button_complete_task = tk.Button(root, text="Complete Task", width=68, command=complete_task)
button_complete_task.pack()
button_save_tasks = tk.Button(root, text="Save Tasks", width=68, command=save_tasks)
button_save_tasks.pack()
button_load_tasks = tk.Button(root, text="Load Tasks", width=68, command=load_tasks)
button_load_tasks.pack()

root.mainloop()
