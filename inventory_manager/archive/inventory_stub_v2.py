#!/usr/bin/python3

from tkinter import *
from tkinter.messagebox import showinfo,showerror
import sqlite3
import hashlib

class InventoryManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Manager")
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()
        self.create_table()
        self.create_gui()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                         (username TEXT PRIMARY KEY, password TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS inventory
                         (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')
        self.conn.commit()

    def create_gui(self):
        # Login frame
        self.login_frame = Frame(self.root)
        self.login_frame.pack()

        Label(self.login_frame, text="Username").pack()
        self.username_entry = Entry(self.login_frame)
        self.username_entry.pack()

        Label(self.login_frame, text="Password").pack()
        self.password_entry = Entry(self.login_frame, show="*")
        self.password_entry.pack()

        Button(self.login_frame, text="Login", command=self.login).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = self.c.fetchone()

        if user:
            self.login_frame.destroy()
            self.create_main_gui()
        else:
            showerror("Error", "Invalid username or password")

    def create_main_gui(self):
        # Main frame
        self.main_frame = Frame(self.root)
        self.main_frame.pack()

        # Labels and entry fields
        Label(self.main_frame, text="Item Name").grid(column=0, row=0)
        Label(self.main_frame, text="Quantity").grid(column=1, row=0)

        self.name_entry = Entry(self.main_frame)
        self.name_entry.grid(column=0, row=1)
        self.quantity_entry = Entry(self.main_frame)
        self.quantity_entry.grid(column=1, row=1)

        # Buttons
        Button(self.main_frame, text="Add Item", command=self.add_item).grid(column=0, row=2)
        Button(self.main_frame, text="View Inventory", command=self.view_inventory).grid(column=1, row=2)
        Button(self.main_frame, text="Delete Item", command=self.delete_item).grid(column=2, row=2)
        Button(self.main_frame, text="Edit Item", command=self.edit_item).grid(column=3, row=2)
        Button(self.main_frame, text="Sort by Name", command=self.sort_by_name).grid(column=0, row=3)
        Button(self.main_frame, text="Sort by Quantity", command=self.sort_by_quantity).grid(column=1, row=3)
        Button(self.main_frame, text="Search", command=self.search).grid(column=2, row=3)

    def add_item(self):
        try:
            name = self.name_entry.get()
            quantity = int(self.quantity_entry.get())
            if name and quantity > 0:
                self.c.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
                self.conn.commit()
                showinfo("Success", "Item added successfully")
            else:
                showerror("Error", "Please enter a valid name and quantity")
        except ValueError:
            showerror("Error", "Please enter a valid quantity")

    def view_inventory(self):
        try:
            self.c.execute("SELECT * FROM inventory")
            rows = self.c.fetchall()
            showinfo("Inventory", "\n".join(str(row) for row in rows))
        except sqlite3.Error as e:
            showerror("Error", str(e))

    def delete_item(self):
        try:
            name = self.name_entry.get()
            if name:
                self.c.execute("DELETE FROM inventory WHERE name=?", (name,))
                self.conn.commit()
                showinfo("Success", "Item deleted successfully")
            else:
                showerror("Error", "Please enter a valid name")
        except sqlite3.Error as e:
            showerror("Error", str(e))

    def edit_item(self):
        try:
            name = self.name_entry.get()
            quantity = int(self.quantity_entry.get())
            if name and quantity > 0:
                self.c.execute("UPDATE inventory SET quantity=? WHERE name=?", (quantity, name))
                self.conn.commit()
                showinfo("Success", "Item updated successfully")
            else:
                showerror("Error", "Please enter a valid name and quantity")
        except ValueError:
            showerror("Error", "Please enter a valid quantity")

    def sort_by_name(self):
        try:
            self.c.execute("SELECT * FROM inventory ORDER BY name")
            rows = self.c.fetchall()
            showinfo("Inventory", "\n".join(str(row) for row in rows))
        except sqlite3.Error as e:
            showerror("Error", str(e))

    def sort_by_quantity(self):
        try:
            self.c.execute("SELECT * FROM inventory ORDER BY quantity")
            rows = self.c.fetchall()
            showinfo("Inventory", "\n".join(str(row) for row in rows))
        except sqlite3.Error as e:
            showerror("Error", str(e))

    def search(self):
        try:
            name = self.name_entry.get()
            if name:
                self.c.execute("SELECT * FROM inventory WHERE name=?", (name,))
                rows = self.c.fetchall()
                if rows:
                    showinfo("Inventory", "\n".join(str(row) for row in rows))
                else:
                    showinfo("Inventory", "Item not found")
            else:
                showerror("Error", "Please enter a valid name")
        except sqlite3.Error as e:
            showerror("Error", str(e))

'''
In this updated version, I've added a login feature that requires users to enter a username and password to access the app. The password is hashed using SHA-256 for security. The app also creates a separate table for users and stores the hashed password in the database.

Note that this is a basic example and you should consider implementing additional security measures, such as salting and peppering passwords, to make your app more secure.
'''

if __name__ == "__main__":
    root = Tk()
    app = InventoryManager(root)
    root.mainloop()
