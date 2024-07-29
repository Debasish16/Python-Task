import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.configure(bg='#023020')

        # Style Configuration
        style = ttk.Style()
        style.configure('TLabel', foreground='white', background='#1e1e1e', font=("Arial", 12))
        style.configure('TButton', foreground='white', background='red', font=("Arial", 12, "bold"))
        style.configure('TCheckbutton', foreground='white', background='#1e1e1e', font=("Arial", 12))

        # Title Label
        self.title_label = ttk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Password Length Label and Entry
        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)
        self.length_entry = ttk.Entry(root, font=("Arial", 12))
        self.length_entry.pack(pady=5)

        # Checkbox Options
        self.uppercase_var = tk.IntVar()
        self.lowercase_var = tk.IntVar()
        self.digits_var = tk.IntVar()
        self.special_var = tk.IntVar()

        self.uppercase_check = ttk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.pack(pady=2)
        self.lowercase_check = ttk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.pack(pady=2)
        self.digits_check = ttk.Checkbutton(root, text="Include Digits", variable=self.digits_var)
        self.digits_check.pack(pady=2)
        self.special_check = ttk.Checkbutton(root, text="Include Special Characters", variable=self.special_var)
        self.special_check.pack(pady=2)

        # Frame for Generate Button
        self.button_frame = tk.Frame(root, bg='#677D6A', highlightbackground="#007ACC", highlightthickness=2)
        self.button_frame.pack(pady=20)
        
        # Generate Button
        self.generate_button = tk.Button(self.button_frame, text="Generate Password", command=self.generate_password, font=("Arial", 12, "bold"), fg="white", bg='#EB3678', bd=0)
        self.generate_button.pack(padx=10, pady=10)

        # Password Display
        self.password_display = ttk.Entry(root, font=("Arial", 12), justify='center')
        self.password_display.pack(pady=5)

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")
            return

        length = int(length)
        if length < 1:
            messagebox.showerror("Invalid Length", "Password length must be at least 1.")
            return

        characters = ''
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("No Characters Selected", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
