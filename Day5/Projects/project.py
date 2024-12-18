import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validLogin():
    userid = username_entry.get()
    confirm = confirm_entry.get()
    password = password_entry.get()
    captcha = captcha_entry.get()

    # Validation logic
    if userid == "Harsh" and password == "password" and confirm == password and captcha == "xyz123":
        messagebox.showinfo("Login Successfully!", "Welcome to my login portal")
    else:
        messagebox.showinfo("Login Failed", "Try again, invalid user id, password, or captcha")

# Create the main window
parent = tk.Tk()
parent.title("LOGIN PORTAL BY HARSH")
parent.geometry("300x300")  # Adjust window size

# Center the window on the screen
window_width = 300
window_height = 300
screen_width = parent.winfo_screenwidth()
screen_height = parent.winfo_screenheight()

# Calculate position x, y for centering the window
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
parent.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Username label and entry
username_label = tk.Label(parent, text="Enter User-id", anchor="w")
username_label.pack(fill="x", padx=10, pady=5, anchor="center")
username_entry = tk.Entry(parent)
username_entry.pack(fill="x", padx=10, pady=5, anchor="center")

# Password label and entry
password_label = tk.Label(parent, text="Enter Password", anchor="w")
password_label.pack(fill="x", padx=10, pady=5, anchor="center")
password_entry = tk.Entry(parent, show="*")
password_entry.pack(fill="x", padx=10, pady=5, anchor="center")

# Confirm password label and entry
confirm_label = tk.Label(parent, text="Confirm Password", anchor="w")
confirm_label.pack(fill="x", padx=10, pady=5, anchor="center")
confirm_entry = tk.Entry(parent, show="*")
confirm_entry.pack(fill="x", padx=10, pady=5, anchor="center")

# Captcha label and entry
captcha_label = tk.Label(parent, text="Enter Captcha :\nxyz123", anchor="w")
captcha_label.pack(fill="x", padx=10, pady=5, anchor="center")
captcha_entry = tk.Entry(parent)
captcha_entry.pack(fill="x", padx=10, pady=5, anchor="center")

# Login button
login_button = tk.Button(parent, text="Login", command=validLogin)
login_button.pack(pady=20, anchor="center")

# Start the Tkinter event loop
parent.mainloop()
