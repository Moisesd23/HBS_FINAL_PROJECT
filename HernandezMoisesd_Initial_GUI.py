"""
Author: Moises Hernandez
Date: 04/25/2025
Assignment: Module 6 Project Status Report II
Short Desc: The HBS application is designed to simplify and streamline the payment and transfer process
for bank customers. It would provide a user-friendly interface that addresses common difficulties experienced
by older adults and those less familiar with digital banking technology.
"""

import tkinter as tk
from tkinter import messagebox

# HBS - Horizon Banking Services
# Initial GUI Setup

# This module initializes the GUI for the HBS application including login and dashboard windows.

def login():
    if not username_entry.get() or not password_entry.get():
        messagebox.showerror("Input Error", "Username and password cannot be empty.")
        return
    open_dashboard()

def open_dashboard():
    login_window.destroy()
    dashboard = tk.Tk()
    dashboard.title("HBS - Dashboard")

    tk.Label(dashboard, text="Welcome to HBS Dashboard", font=("Arial", 18)).pack(pady=10)

    tk.Button(dashboard, text="Make a Payment", command=make_payment).pack(pady=5)
    tk.Button(dashboard, text="Transfer to Another Account", command=transfer).pack(pady=5)
    tk.Button(dashboard, text="Exit", command=dashboard.quit).pack(pady=5)

    dashboard.mainloop()

def make_payment():
    messagebox.showinfo("Make a Payment", "Payment window will be implemented here.")

def transfer():
    messagebox.showinfo("Transfer", "Transfer window will be implemented here.")

# Login Window Setup
login_window = tk.Tk()
login_window.title("HBS - Login")

# Variables
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Buttons
tk.Button(login_window, text="Login", command=login).pack(pady=5)
tk.Button(login_window, text="Exit", command=login_window.quit).pack(pady=5)

login_window.mainloop()
