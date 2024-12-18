import tkinter as tk
from tkinter import messagebox
# Function to validate the login

def validLogin():                               # First Part..
    userid = username_entry.get()
    confirm = confirm_entry.get()
    password = password_entry.get()
    captcha = captcha_entry.get()

    # You can add your own validation login here

    if userid == "Harsh" and password == "password" and confirm ==password and captcha=="xyz123":
        messagebox.showinfo("Login Successfully !","Welcome to my login portal")
    else :
        messagebox.showinfo("Login Failed","Try again invalid user id or password")

# Create the main Window   # Part 2..

parent = tk.Tk()
parent.title("LOGIN PORTAL BY HARSH")

username_label = tk.Label(parent,text="Enter User-id")
username_label.pack()               # Fix kar na in window
username_entry = tk.Entry(parent)  # Window me permission to print
username_entry.pack()

username_label = tk.Label(parent,text="Enter Password")
username_label.pack()
password_entry = tk.Entry(parent,show="*")
password_entry.pack()

confirm_label = tk.Label(parent,text="Confirm Password")
confirm_label.pack()
confirm_entry = tk.Entry(parent,show="*")
confirm_entry.pack()

captcha_label = tk.Label(parent,text="Enter Captcha :\nxyz123")
captcha_label.pack()
captcha_entry = tk.Entry(parent)
captcha_entry.pack()
login_label = tk.Label(parent,text="\n")
login_button = tk.Button(parent,text="Login",command=validLogin)
login_button.pack()

 # To Run Code
login_button.mainloop()





