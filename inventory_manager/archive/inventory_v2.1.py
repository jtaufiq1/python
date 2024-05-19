#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from sqlite3 import Error
import hashlib

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to {db_file} established")
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
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
        sql_create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY,
            username text NOT NULL UNIQUE,
            password text NOT NULL
        );
        """
        sql_create_sales_table = """
        CREATE TABLE IF NOT EXISTS sales (
            id integer PRIMARY KEY,
            item_id integer,
            quantity integer,
            total_price real,
            sale_date text,
            FOREIGN KEY (item_id) REFERENCES inventory (id)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_inventory_table)
        cursor.execute(sql_create_users_table)
        cursor.execute(sql_create_sales_table)
        print("Tables created")
    except Error as e:
        print(e)

def add_user(conn, user):
    """Add a new user to the users table"""
    sql = '''INSERT INTO users(username, password)
             VALUES(?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, user)
    conn.commit()
    return cursor.lastrowid

def check_user(conn, username, password):
    """Check if the username and password match any entry in the users table"""
    sql = '''SELECT * FROM users WHERE username=? AND password=?'''
    cursor = conn.cursor()
    cursor.execute(sql, (username, hashlib.sha256(password.encode()).hexdigest()))
    return cursor.fetchone()

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

def log_sale(conn, sale):
    """Log a sale in the sales table"""
    sql = '''INSERT INTO sales(item_id, quantity, total_price, sale_date)
             VALUES(?, ?, ?, datetime('now'))'''
    cursor = conn.cursor()
    cursor.execute(sql, sale)
    conn.commit()
    return cursor.lastrowid

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.conn = create_connection("inventory.db")
        create_tables(self.conn)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Password").grid(row=1, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.signup_button = tk.Button(self.root, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if check_user(self.conn, username, password):
            self.root.destroy()
            root = tk.Tk()
            InventoryApp(root, username == "admin")
            root.mainloop()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            try:
                add_user(self.conn, (username, hashed_password))
                messagebox.showinfo("Success", "User registered successfully")
            except sqlite3.IntegrityError:
                messagebox.showerror("Signup Error", "Username already exists")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

class InventoryApp:
    def __init__(self, root, is_admin):
        self.root = root
        self.root.title("Inventory App")

        self.conn = create_connection("inventory.db")

        self.is_admin = is_admin

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

        self.sale_button = tk.Button(self.root, text="Sale Item", command=self.sale_item)
        self.sale_button.grid(row=1, column=6, padx=10, pady=10)

        if self.is_admin:
            self.add_user_button = tk.Button(self.root, text="Add User", command=self.add_user)
            self.add_user_button.grid(row=1, column=7, padx=10, pady=10)

        # Treeview (for displaying items)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=2, column=0, columnspan=8, padx=10, pady=10)

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

    def sale_item(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to sell")
            return
        item_id = self.tree.item(selected_item)["values"][0]
        top = tk.Toplevel(self.root)
        top.title("Sale Item")

        tk.Label(top, text="Quantity").grid(row=0, column=0, padx=10, pady=10)
        quantity_entry = tk.Entry(top)
        quantity_entry.grid(row=0, column=1, padx=10, pady=10)

        def process_sale():
            quantity = quantity_entry.get()
            item = self.tree.item(selected_item)["values"]
            if quantity:
                total_price = item[3] * int(quantity)
                log_sale(self.conn, (item_id, int(quantity), total_price))
                update_item(self.conn, (item[2] - int(quantity), item[3], item_id))
                self.load_items()
                top.destroy()
                messagebox.showinfo("Sale Success", f"Item sold for {total_price}")
            else:
                messagebox.showwarning("Input Error", "Please enter a quantity")

        tk.Button(top, text="Process Sale", command=process_sale).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def add_user(self):
        top = tk.Toplevel(self.root)
        top.title("Add User")

        tk.Label(top, text="Username").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(top, text="Password").grid(row=1, column=0, padx=10, pady=10)

        username_entry = tk.Entry(top)
        username_entry.grid(row=0, column=1, padx=10, pady=10)
        password_entry = tk.Entry(top, show='*')
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        def add_user_to_db():
            username = username_entry.get()
            password = password_entry.get()
            if username and password:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                try:
                    add_user(self.conn, (username, hashed_password))
                    messagebox.showinfo("Success", "User added successfully")
                    top.destroy()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Username already exists")
            else:
                messagebox.showwarning("Input Error", "Please fill out all fields")

        tk.Button(top, text="Add User", command=add_user_to_db).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def load_items(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = select_all_items(self.conn)
        for row in rows:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
