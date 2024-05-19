Adding documentation and help to the script involves adding comments to explain various parts of the code and providing user assistance through pop-up messages or tooltips. Here's the modified script with added documentation and help:

```python
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from sqlite3 import Error
import hashlib
import os
import binascii
from datetime import datetime, timedelta

# Utility functions

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to {db_file} established")
    except Error as e:
        print(e)
    return conn

# Function to create database tables
def create_tables(conn):
    """Create tables in the SQLite database."""
    try:
        # SQL statements to create tables
        sql_create_inventory_table = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER,
            price REAL
        );
        """
        sql_create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            salt TEXT NOT NULL
        );
        """
        sql_create_sales_table = """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            item_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            sale_date TEXT,
            FOREIGN KEY (item_id) REFERENCES inventory (id)
        );
        """
        # Execute SQL statements
        cursor = conn.cursor()
        cursor.execute(sql_create_inventory_table)
        cursor.execute(sql_create_users_table)
        cursor.execute(sql_create_sales_table)
        print("Tables created")
    except Error as e:
        print(e)

# Function to generate a salt for password hashing
def generate_salt():
    """Generate a salt for hashing passwords."""
    return binascii.b2a_hex(os.urandom(16)).decode('utf-8')

# Function to hash a password with a given salt
def hash_password(password, salt):
    """Hash a password with a given salt."""
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Function to add a new user to the users table
def add_user(conn, user):
    """Add a new user to the users table."""
    sql = '''INSERT INTO users(username, password, salt)
             VALUES(?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, user)
    conn.commit()
    return cursor.lastrowid

# Function to check if the username and password match any entry in the users table
def check_user(conn, username, password):
    """Check if the username and password match any entry in the users table."""
    sql = '''SELECT * FROM users WHERE username=?'''
    cursor = conn.cursor()
    cursor.execute(sql, (username,))
    user = cursor.fetchone()
    if user:
        user_id, username, hashed_password, salt = user
        if hashed_password == hash_password(password, salt):
            return True
    return False

# Function to add a new item to the inventory table
def add_item(conn, item):
    """Add a new item to the inventory table."""
    sql = '''INSERT INTO inventory(name, quantity, price)
             VALUES(?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, item)
    conn.commit()
    return cursor.lastrowid

# Function to update quantity and price of an item in the inventory table
def update_item(conn, item):
    """Update quantity and price of an item in the inventory table."""
    sql = '''UPDATE inventory
             SET quantity = ?,
                 price = ?
             WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, item)
    conn.commit()

# Function to delete an item from the inventory table by id
def delete_item(conn, item_id):
    """Delete an item from the inventory table by id."""
    sql = 'DELETE FROM inventory WHERE id=?'
    cursor = conn.cursor()
    cursor.execute(sql, (item_id,))
    conn.commit()

# Function to query all rows in the inventory table
def select_all_items(conn):
    """Query all rows in the inventory table."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    return rows

# Function to search items in the inventory table by name
def search_items(conn, search_query):
    """Search items in the inventory table by name."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + search_query + '%',))
    rows = cursor.fetchall()
    return rows

# Function to sort items in the inventory table
def sort_items(conn, column, order):
    """Sort items in the inventory table."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM inventory ORDER BY {column} {order}")
    rows = cursor.fetchall()
    return rows

# Function to log a sale in the sales table
def log_sale(conn, sale):
    """Log a sale in the sales table."""
    sql = '''INSERT INTO sales(item_id, quantity, total_price, sale_date)
             VALUES(?, ?, ?, datetime('now'))'''
    cursor = conn.cursor()
    cursor.execute(sql, sale)
    conn.commit()
    return cursor.lastrowid

# Function to get sales report for the last `days` days
def get_sales_report(conn, days):
    """Get sales report for the last `days` days."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales WHERE sale_date >= date('now', ?)", (f'-{days} days',))
    rows = cursor.fetchall()
    return rows

# Class for the login window
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
            salt = generate_salt()
            hashed_password = hash_password(password, salt)
            try:
                add_user(self.conn, (username, hashed_password, salt))
                messagebox.showinfo("Success", "User registered successfully")
                self.clear_entries()
            except sqlite3.IntegrityError:
                messagebox.showerror("Signup Error", "Username already exists")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def clear_entries(self):
        """Clear the input fields."""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
