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
        
        
        self.label = tk.Label(root, text="Task:")
        self.label.pack()
        
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        
        
        self.add_button = tk.Button(root, text="Add Task",bg='lightpink', command=self.add_task)
        self.add_button.pack()
        
        
        self.task_list = tk.Listbox(root)
        self.task_list.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
