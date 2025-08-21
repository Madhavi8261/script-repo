import tkinter as tk
from tkinter import messagebox

def login(username, password):
    """Login logic to be tested by Robot Framework."""
    if username == "admin" and password == "password123":
        return True
    return False

def login_gui():
    """GUI login handler."""
    username = entry_username.get()
    password = entry_password.get()
    if login(username, password):
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Credentials")

# GUI Setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("300x200")

    # Username
    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    # Password
    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Login Button
    login_button = tk.Button(root, text="Login", command=login_gui)
    login_button.pack(pady=20)

    root.mainloop()
