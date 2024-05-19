#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to {db_file} established")
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create tables in the SQLite database"""
    try:
        sql_create_inventory_table = """
        CREATE TABLE IF NOT EXISTS inventory (
            id integer PRIMARY KEY,
            name text NOT NULL,
            quantity integer,
            price real
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_inventory_table)
        print("Inventory table created")
    except Error as e:
        print(e)

def add_item(conn, item):
    """Add a new item to the inventory table"""
    sql = '''INSERT INTO inventory(name, quantity, price)
             VALUES(?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, item)
    conn.commit()
    return cursor.lastrowid

def update_item(conn, item):
    """Update quantity and price of an item in the inventory table"""
    sql = '''UPDATE inventory
             SET quantity = ?,
                 price = ?
             WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, item)
    conn.commit()

def delete_item(conn, item_id):
    """Delete an item from the inventory table by id"""
    sql = 'DELETE FROM inventory WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (item_id,))
    conn.commit()

def select_all_items(conn):
    """Query all rows in the inventory table"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    return rows

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory App")

        self.conn = create_connection("inventory.db")
        create_table(self.conn)

        self.create_widgets()
        self.load_items()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Quantity").grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Price").grid(row=0, column=2, padx=10, pady=10)

        # Entry fields
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=2, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=1, column=3, padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Item", command=self.update_item)
        self.update_button.grid(row=1, column=4, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Item", command=self.delete_item)
        self.delete_button.grid(row=1, column=5, padx=10, pady=10)

        # Treeview (for displaying items)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

    def add_item(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name and quantity and price:
            add_item(self.conn, (name, int(quantity), float(price)))
            self.load_items()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def update_item(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to update")
            return
        item_id = self.tree.item(selected_item)["values"][0]
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name and quantity and price:
            update_item(self.conn, (int(quantity), float(price), item_id))
            self.load_items()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def delete_item(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to delete")
            return
        item_id = self.tree.item(selected_item)["values"][0]
        delete_item(self.conn, item_id)
        self.load_items()

    def load_items(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = select_all_items(self.conn)
        for row in rows:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

