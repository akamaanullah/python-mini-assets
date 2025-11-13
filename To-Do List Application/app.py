import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass

# Create GUI
root = tk.Tk()
root.title("To-Do List")

entry_task = tk.Entry(root, width=40)
entry_task.pack()

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.pack()

listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack()

button_delete = tk.Button(root, text="Delete Task", command=delete_task)
button_delete.pack()

root.mainloop()
