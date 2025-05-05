"""
Author: Moises Hernandez
Date: 05/05/2025
Module 08 Final Project Submission
Description:
The HBS application is designed to simplify and streamline the payment and transfer process
for bank customers. It provides a user-friendly interface that addresses common difficulties
experienced by older adults and those less familiar with digital banking technology.
"""

import tkinter as tk
from tkinter import messagebox  # For popup alerts
from tkinter import PhotoImage  # To display images

# ---------------------------
# Callback Functions
# ---------------------------

def login():
    """Validates login credentials and opens the dashboard window if input is valid."""
    # Check if username and password fields are filled
    if not username_entry.get() or not password_entry.get():
        messagebox.showerror("Input Error", "Username and password cannot be empty.")
        return
    open_dashboard()  # Proceed to dashboard

def open_dashboard():
    """Destroys the login window and opens the main dashboard."""
    login_window.destroy()  # Close login window
    dashboard = tk.Tk()
    dashboard.title("HBS - Dashboard")

    # Attempt to display bank logo
    try:
        logo = PhotoImage(file="HBS_LOGO.png")  # Logo image file
        tk.Label(dashboard, image=logo).pack()
        tk.Label(dashboard, text="Discovering New Horizons").pack()
        dashboard.logo = logo  # Keep a reference to avoid garbage collection
    except:
        tk.Label(dashboard, text="[Bank Logo Image Placeholder]").pack()

    # Dashboard heading
    tk.Label(dashboard, text="Welcome to HBS Dashboard", font=("Arial", 18)).pack(pady=10)

    # Feature buttons
    tk.Button(dashboard, text="Make a Payment", command=lambda: make_payment(dashboard)).pack(pady=5)
    tk.Button(dashboard, text="Transfer to Another Account", command=lambda: transfer(dashboard)).pack(pady=5)
    tk.Button(dashboard, text="Internal Transfer", command=lambda: internal_transfer(dashboard)).pack(pady=5)
    tk.Button(dashboard, text="Exit", command=dashboard.quit).pack(pady=5)

    dashboard.mainloop()

def make_payment(parent):
    """Creates a new window for submitting a payment."""
    payment_window = tk.Toplevel(parent)
    payment_window.title("Make a Payment")

    # Form Fields
    tk.Label(payment_window, text="Recipient Name:").pack()
    recipient_entry = tk.Entry(payment_window)  # Input for recipient name
    recipient_entry.pack()

    tk.Label(payment_window, text="Amount:").pack()
    amount_entry = tk.Entry(payment_window)  # Input for amount
    amount_entry.pack()

    tk.Label(payment_window, text="Purpose:").pack()
    purpose_entry = tk.Entry(payment_window)  # Input for purpose
    purpose_entry.pack()

    # Try to show profile image or fallback text
    try:
        card_img = PhotoImage(file="generic-profile-placeholder-icon-nqu0ajnbs6wkw14q.png")
        tk.Label(payment_window, image=card_img).pack()
        tk.Label(payment_window, text="User Payment Icon").pack()
        payment_window.card_img = card_img  # Keep image reference
    except:
        tk.Label(payment_window, text="[Card Icon Placeholder]").pack()

    def submit_payment():
        """Validates and submits payment form."""
        # Validation checks
        if not recipient_entry.get() or not amount_entry.get() or not purpose_entry.get():
            messagebox.showerror("Input Error", "All fields must be filled.")
            return
        try:
            float(amount_entry.get())  # Ensure amount is a number
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
            return
        messagebox.showinfo("Success", "Payment submitted successfully!")  # Success message
        payment_window.destroy()

    # Action buttons
    tk.Button(payment_window, text="Submit", command=submit_payment).pack(pady=5)
    tk.Button(payment_window, text="Cancel", command=payment_window.destroy).pack()

def transfer(parent):
    """Creates a new window for transferring money to another account."""
    transfer_window = tk.Toplevel(parent)
    transfer_window.title("Transfer to Another Account")

    # Form Fields
    tk.Label(transfer_window, text="Recipient Account Number:").pack()
    account_entry = tk.Entry(transfer_window)  # Input for account number
    account_entry.pack()

    tk.Label(transfer_window, text="Transfer Amount:").pack()
    transfer_amount_entry = tk.Entry(transfer_window)  # Input for amount
    transfer_amount_entry.pack()

    def submit_transfer():
        """Validates and submits external transfer form."""
        if not account_entry.get() or not transfer_amount_entry.get():
            messagebox.showerror("Input Error", "All fields must be filled.")
            return
        try:
            float(transfer_amount_entry.get())  # Check amount is numeric
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
            return
        messagebox.showinfo("Success", "Transfer completed successfully!")  # Success alert
        transfer_window.destroy()

    # Action buttons
    tk.Button(transfer_window, text="Submit", command=submit_transfer).pack(pady=5)
    tk.Button(transfer_window, text="Cancel", command=transfer_window.destroy).pack()

def internal_transfer(parent):
    """Creates a new window for internal account transfers."""
    internal_window = tk.Toplevel(parent)
    internal_window.title("Internal Transfer")

    # Form Fields
    tk.Label(internal_window, text="From Account:").pack()
    from_account = tk.Entry(internal_window)  # Sender account
    from_account.pack()

    tk.Label(internal_window, text="To Account:").pack()
    to_account = tk.Entry(internal_window)  # Receiver account
    to_account.pack()

    tk.Label(internal_window, text="Amount:").pack()
    transfer_amount = tk.Entry(internal_window)  # Transfer amount
    transfer_amount.pack()

    def submit_internal():
        """Validates and submits internal transfer form."""
        if not from_account.get() or not to_account.get() or not transfer_amount.get():
            messagebox.showerror("Input Error", "All fields must be filled.")
            return
        try:
            float(transfer_amount.get())  # Ensure amount is a number
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
            return
        messagebox.showinfo("Success", "Internal transfer successful!")  # Success alert
        internal_window.destroy()

    # Action buttons
    tk.Button(internal_window, text="Submit", command=submit_internal).pack(pady=5)
    tk.Button(internal_window, text="Cancel", command=internal_window.destroy).pack()

# ---------------------------
# Login Window Setup
# ---------------------------

# Create main login window
login_window = tk.Tk()
login_window.title("HBS - Login")

# Username entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)  # User input for username
username_entry.pack()

# Password entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")  # User input for password (hidden)
password_entry.pack()

# Login and Exit buttons
tk.Button(login_window, text="Login", command=login).pack(pady=5)  # Call login
tk.Button(login_window, text="Exit", command=login_window.quit).pack(pady=5)  # Exit app

# Run the application
login_window.mainloop()
