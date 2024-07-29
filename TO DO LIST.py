import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Main application class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stunning To-Do List")
        self.root.geometry("600x600")

        # Set background color
        self.root.configure(bg='#334139')

        self.tasks = []

        # Setting up the main frame
        self.frame = tk.Frame(self.root, bg='#f0f0f0')
        self.frame.pack(pady=20)

        # Creating the input field
        self.task_input = tk.Entry(self.frame, width=35, font=("Times new roman", 14), bg='#e6e6e6', fg='#333')
        self.task_input.pack(side=tk.LEFT, padx=10)

        # Creating styled buttons
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg='#4CAF50', fg='white', font=("Arial", 12, 'bold'), relief='flat')
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg='#f44336', fg='white', font=("Arial", 12, 'bold'), relief='flat')
        self.delete_button.pack(pady=5)

        self.visualize_button = tk.Button(self.root, text="Visualize Tasks", command=self.visualize_tasks, bg='#2196F3', fg='white', font=("Arial", 12, 'bold'), relief='flat')
        self.visualize_button.pack(pady=5)

        # Creating the listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Times new roman", 14), bg='#83CACD', fg='#333', selectbackground='#dcdcdc', selectforeground='#000')
        self.task_listbox.pack(pady=20)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def visualize_tasks(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to visualize.")
            return

        task_lengths = [len(task) for task in self.tasks]
        fig, ax = plt.subplots()
        ax.barh(self.tasks, task_lengths, color='skyblue')
        ax.set_xlabel('Task Length')
        ax.set_ylabel('Tasks')
        ax.set_title('Task Length Visualization')
        plt.show()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
