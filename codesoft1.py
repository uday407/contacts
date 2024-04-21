import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
   
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}"

class ContactManager:
    def __init__(self):
        self.contacts = []
   
    def add_contact(self, name, phone_number, email, address):
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
   
    def view_contact_list(self):
        return self.contacts
   
    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts
   
    def update_contact(self, old_name, new_name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
   
    def delete_contact(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[idx]
                break

class ContactManagerApp:
    def __init__(self, root):
        self.contact_manager = ContactManager()
       
        # GUI setup
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("500x400")
       
        # Labels and Entry Widgets
        tk.Label(root, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
       
        tk.Label(root, text="Phone Number:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
       
        tk.Label(root, text="Email:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
       
        tk.Label(root, text="Address:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
       
        # Buttons
        add_button = tk.Button(root, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        add_button.grid(row=4, column=0, columnspan=2, pady=10)
       
        view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, font=("Arial", 12))
        view_button.grid(row=5, column=0, columnspan=2, pady=5)
       
        search_button = tk.Button(root, text="Search Contact", command=self.search_contact, font=("Arial", 12))
        search_button.grid(row=6, column=0, columnspan=2, pady=5)
       
        update_button = tk.Button(root, text="Update Contact", command=self.update_contact, font=("Arial", 12))
        update_button.grid(row=7, column=0, columnspan=2, pady=5)
       
        delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12))
        delete_button.grid(row=8, column=0, columnspan=2, pady=5)
   
    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone_number:
            self.contact_manager.add_contact(name, phone_number, email, address)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required.")
   
    def view_contacts(self):
        contacts = self.contact_manager.view_contact_list()
        if not contacts:
            messagebox.showinfo("No Contacts", "Contact list is empty.")
        else:
            contact_info = "\n".join(str(contact) for contact in contacts)
            messagebox.showinfo("Contact List", contact_info)
   
    def search_contact(self):
        search_term = self.name_entry.get()  # Use name field for search term
        if search_term:
            found_contacts = self.contact_manager.search_contact(search_term)
            if not found_contacts:
                messagebox.showinfo("No Match", "No contacts found.")
            else:
                contact_info = "\n".join(str(contact) for contact in found_contacts)
                messagebox.showinfo("Search Results", contact_info)
        else:
            messagebox.showerror("Error", "Please enter a search term.")
   
    def update_contact(self):
        old_name = self.name_entry.get()
        new_name = self.phone_entry.get()
        new_phone_number = self.email_entry.get()
        new_email = self.address_entry.get()
        new_address = self.address_entry.get()
        if old_name and new_name:
            self.contact_manager.update_contact(old_name, new_name, new_phone_number, new_email, new_address)
            messagebox.showinfo("Success", "Contact updated successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please provide old and new contact names.")
   
    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            self.contact_manager.delete_contact(name)
            messagebox.showinfo("Success", "Contact deleted successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter the name of the contact to delete.")
   
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()