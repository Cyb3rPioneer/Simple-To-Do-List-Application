import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import csv

# Main window
root = tk.Tk()
root.title("Enhanced To-Do List Application")
root.geometry("600x500")
root.config(bg="#f2f2f2")

# Task list
tasks = []

# Update task list function
def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        display_text = f"{task['name']} - {task['status']} - {task['priority']} - {task['date']}"
        listbox_tasks.insert(tk.END, display_text)
        if task['status'] == "Completed":
            listbox_tasks.itemconfig(listbox_tasks.size() - 1, {'bg': 'lightgreen'})
        else:
            listbox_tasks.itemconfig(listbox_tasks.size() - 1, {'bg': 'lightcoral'})

# Add task function
def add_task():
    task_name = entry_task.get()
    priority = priority_var.get()
    if task_name and priority:
        tasks.append({"name": task_name, "status": "Not Completed", "priority": priority, "date": datetime.now().strftime("%Y-%m-%d")})
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task name and priority cannot be empty.")

# Edit task function
def edit_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        new_name = entry_task.get()
        tasks[task_index]["name"] = new_name
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Delete task function
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Mark task as completed function
def mark_completed():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks[task_index]["status"] = "Completed"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Save tasks to CSV
def save_tasks():
    with open("tasks.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Status", "Priority", "Date"])
        for task in tasks:
            writer.writerow([task['name'], task['status'], task['priority'], task['date']])
    messagebox.showinfo("Info", "Tasks have been saved.")

# Load tasks from CSV
def load_tasks():
    try:
        with open("tasks.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append({"name": row["Name"], "status": row["Status"], "priority": row["Priority"], "date": row["Date"]})
        update_task_list()
        messagebox.showinfo("Info", "Tasks have been loaded.")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Task file not found.")

# Calculate completion percentage
def completion_percentage():
    completed_tasks = sum(1 for task in tasks if task['status'] == "Completed")
    percentage = (completed_tasks / len(tasks)) * 100 if tasks else 0
    messagebox.showinfo("Completion Percentage", f"Tasks are {percentage:.2f}% completed.")

# GUI elements
label_task = tk.Label(root, text="Task:", bg="#f2f2f2")
label_task.pack()

entry_task = tk.Entry(root, width=30)
entry_task.pack()

priority_var = tk.StringVar(value="Normal")
priority_menu = tk.OptionMenu(root, priority_var, "Low", "Normal", "High")
priority_menu.pack()

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack()

button_edit_task = tk.Button(root, text="Edit Task", command=edit_task)
button_edit_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack()

button_mark_completed = tk.Button(root, text="Mark as Completed", command=mark_completed)
button_mark_completed.pack()

button_save_tasks = tk.Button(root, text="Save Tasks", command=save_tasks)
button_save_tasks.pack()

button_load_tasks = tk.Button(root, text="Load Tasks", command=load_tasks)
button_load_tasks.pack()

button_completion_percentage = tk.Button(root, text="Completion Percentage", command=completion_percentage)
button_completion_percentage.pack()

listbox_tasks = tk.Listbox(root, width=70, height=15)
listbox_tasks.pack(pady=10)

# Run the application
root.mainloop()
