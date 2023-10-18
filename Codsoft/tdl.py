import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.label = tk.Label(
            self.root,
            text='To Do List',
            font=('Arial', 25, 'bold'),
            width=10,
            bd=5,
            bg='purple',
            fg='black'
        )
        self.label.pack(side='top', fill=tk.BOTH)
        self.tasks = []
        
        # Create a label
        self.label = tk.Label(root, text="Task:")
        self.label.pack()
        
        # Create an entry field
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        
        # Create an "Add Task" button
        self.add_button = tk.Button(root, text="Add Task", bg='lightpink', command=self.add_task)
        self.add_button.pack()
        
        # Create a "Clear" button
        self.clear_button = tk.Button(root, text="Clear", bg='lightcoral', command=self.clear_task_entry)
        self.clear_button.pack()
        
        # Create a listbox to display tasks
        self.task_list = tk.Listbox(root)
        self.task_list.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def clear_task_entry(self):
        self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
