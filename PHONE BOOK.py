import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        refresh_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")

# Function to refresh the contact list display
def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for contacts
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number:")
    if search_term:
        contact_listbox.delete(0, tk.END)
        for contact in contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update a selected contact
def update_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        contact = contacts[selected_index]
        
        new_name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact['name'])
        new_phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contact['phone'])
        new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact['email'])
        new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact['address'])
        
        if new_name and new_phone:
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            refresh_contact_list()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a contact.")

# Function to delete a selected contact
def delete_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        contacts.pop(selected_index)
        refresh_contact_list()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a contact.")

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x580")
root.configure(bg='#e6e6fa')

# Initialize contacts list
contacts = []

# Define styles
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 10)
button_font = ("times ew roman", 10, "bold")
button_style = {'bg': '#9370db', 'fg': 'black', 'activebackground': '#afeeee', 'activeforeground': 'red'}
listbox_font = ("Helvetica", 10)

# Create entry widgets to add contacts
tk.Label(root, text="Name:", font=label_font, bg='#dda0dd').grid(row=0, column=0, padx=10, pady=5, sticky='e')
name_entry = tk.Entry(root, font=entry_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", font=label_font, bg='#dda0dd').grid(row=1, column=0, padx=10, pady=5, sticky='e')
phone_entry = tk.Entry(root, font=entry_font)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", font=label_font, bg='#dda0dd').grid(row=2, column=0, padx=10, pady=5, sticky='e')
email_entry = tk.Entry(root, font=entry_font)
email_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Address:", font=label_font, bg='#dda0dd').grid(row=3, column=0, padx=10, pady=5, sticky='e')
address_entry = tk.Entry(root, font=entry_font)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons to add, update, delete, and search contacts
tk.Button(root, text="Add Contact", font=button_font, **button_style, command=add_contact).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Update Contact", font=button_font, **button_style, command=update_contact).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Delete Contact", font=button_font, **button_style, command=delete_contact).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Search Contact", font=button_font, **button_style, command=search_contact).grid(row=7, column=0, columnspan=2, pady=10)

# Create a listbox to display contacts
contact_listbox = tk.Listbox(root, width=50, font=listbox_font)
contact_listbox.grid(row=8, column=0, columnspan=2, padx=25, pady=50)

# Run the main event loop
root.mainloop()
