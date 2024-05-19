#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from sqlite3 import Error
import hashlib
from datetime import datetime, timedelta

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

def search_items(conn, search_query):
    """Search items in the inventory table by name"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + search_query + '%',))
    rows = cursor.fetchall()
    return rows

def sort_items(conn, column, order):
    """Sort items in the inventory table"""
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM inventory ORDER BY {column} {order}")
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

def get_sales_report(conn, days):
    """Get sales report for the last `days` days"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales WHERE sale_date >= date('now', ?)", (f'-{days} days',))
    rows = cursor.fetchall()
    return rows

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
        # Search and Sort
        tk.Label(self.root, text="Search").grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_items)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        tk.Label(self.root, text="Sort By").grid(row=0, column=3, padx=10, pady=10)
        self.sort_by = ttk.Combobox(self.root, values=["name", "quantity", "price"])
        self.sort_by.grid(row=0, column=4, padx=10, pady=10)
        self.sort_order = ttk.Combobox(self.root, values=["ASC", "DESC"])
        self.sort_order.grid(row=0, column=5, padx=10, pady=10)
        self.sort_button = tk.Button(self.root, text="Sort", command=self.sort_items)
        self.sort_button.grid(row=0, column=6, padx=10, pady=10)

        # Buttons
        self.manage_button = tk.Button(self.root, text="Manage Stock", command=self.open_manage_stock)
        self.manage_button.grid(row=1, column=0, padx=10, pady=10)
        self.sales_button = tk.Button(self.root, text="Sales", command=self.open_sales)
        self.sales_button.grid(row=1, column=1, padx=10, pady=10)
        self.report_button = tk.Button(self.root, text="Report", command=self.open_report)
        self.report_button.grid(row=1, column=2, padx=10, pady=10)

        # Treeview (for displaying items)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=2, column=0, columnspan=7, padx=10, pady=10)

    def search_items(self):
        search_query = self.search_entry.get()
        if search_query:
            rows = search_items(self.conn, search_query)
            self.load_treeview(rows)
        else:
            self.load_items()

    def sort_items(self):
        column = self.sort_by.get()
        order = self.sort_order.get()
        if column and order:
            rows = sort_items(self.conn, column, order)
            self.load_treeview(rows)
        else:
            self.load_items()

    def load_treeview(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def load_items(self):
        rows = select_all_items(self.conn)
        self.load_treeview(rows)

    def open_manage_stock(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = ManageStockApp(self.new_window, self.conn, self.load_items)

    def open_sales(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = SalesApp(self.new_window, self.conn, self.load_items)

    def open_report(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = ReportApp(self.new_window, self.conn)

class ManageStockApp:
    def __init__(self, root, conn, reload_inventory_callback):
        self.root = root
        self.root.title("Manage Stock")
        self.conn = conn
        self.reload_inventory_callback = reload_inventory_callback

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Quantity").grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Price").grid(row=0, column=2, padx=10, pady=10)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=2, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=1, column=3, padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Item", command=self.update_item)
        self.update_button.grid(row=1, column=4, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Item", command=self.delete_item)
        self.delete_button.grid(row=1, column=5, padx=10, pady=10)

    def add_item(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name and quantity and price:
            add_item(self.conn, (name, int(quantity), float(price)))
            self.reload_inventory_callback()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def update_item(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name and quantity and price:
            update_item(self.conn, (int(quantity), float(price), self.get_item_id(name)))
            self.reload_inventory_callback()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def delete_item(self):
        name = self.name_entry.get()
        if name:
            delete_item(self.conn, self.get_item_id(name))
            self.reload_inventory_callback()
        else:
            messagebox.showwarning("Input Error", "Please enter the name of the item to delete")

    def get_item_id(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM inventory WHERE name=?", (name,))
        return cursor.fetchone()[0]

class SalesApp:
    def __init__(self, root, conn, reload_inventory_callback):
        self.root = root
        self.root.title("Sales")
        self.conn = conn
        self.reload_inventory_callback = reload_inventory_callback

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Item Name").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Quantity").grid(row=0, column=1, padx=10, pady=10)

        self.item_name_entry = tk.Entry(self.root)
        self.item_name_entry.grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        self.sale_button = tk.Button(self.root, text="Make Sale", command=self.make_sale)
        self.sale_button.grid(row=1, column=2, padx=10, pady=10)

    def make_sale(self):
        item_name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        if item_name and quantity:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, quantity, price FROM inventory WHERE name=?", (item_name,))
            item = cursor.fetchone()
            if item and item[1] >= int(quantity):
                total_price = item[2] * int(quantity)
                log_sale(self.conn, (item[0], int(quantity), total_price))
                update_item(self.conn, (item[1] - int(quantity), item[2], item[0]))
                self.reload_inventory_callback()
                messagebox.showinfo("Sale Success", f"Item sold for {total_price}")
            else:
                messagebox.showwarning("Error", "Insufficient stock or item not found")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

class ReportApp:
    def __init__(self, root, conn):
        self.root = root
        self.root.title("Sales Report")
        self.conn = conn

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Report Type").grid(row=0, column=0, padx=10, pady=10)
        self.report_type = ttk.Combobox(self.root, values=["Daily", "Weekly", "Monthly"])
        self.report_type.grid(row=0, column=1, padx=10, pady=10)
        self.report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=0, column=2, padx=10, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Item ID", "Quantity", "Total Price", "Sale Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Item ID", text="Item ID")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Total Price", text="Total Price")
        self.tree.heading("Sale Date", text="Sale Date")
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def generate_report(self):
        report_type = self.report_type.get()
        if report_type == "Daily":
            days = 1
        elif report_type == "Weekly":
            days = 7
        elif report_type == "Monthly":
            days = 30
        else:
            messagebox.showwarning("Input Error", "Please select a report type")
            return

        rows = get_sales_report(self.conn, days)
        self.load_treeview(rows)

    def load_treeview(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
