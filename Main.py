import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# User data (replace with your own data or implement a database)
user_data = {"techtetris": {"password": "1234", "secret_code": "fiem"}}


def function1():
    os.system("FaceBasedAttendenceSystem.py")  # Call your function here


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the entered username exists
    if username in user_data:
        # Check if the entered password matches the stored password
        if password == user_data[username]["password"]:
            function1()  # Call the function1 after a successful login
        else:
            messagebox.showerror("Login Failed", "Invalid password")
    else:
        messagebox.showerror("Login Failed", "Username not found")


def forgot_password():
    username = username_entry.get()
    if username in user_data:
        secret_code = user_data[username]["secret_code"]
        entered_secret_code = simpledialog.askstring(
            "Secret Code", "Enter your secret code:"
        )
        if entered_secret_code == secret_code:
            messagebox.showinfo(
                "Forgot Password",
                f"Your password is: {user_data[username]['password']}",
            )
        else:
            messagebox.showerror("Forgot Password", "Incorrect secret code")
    else:
        messagebox.showerror("Forgot Password", "Username not found")


def on_resize(event):
    # Update the background image and label size
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(resized_image)
    background_label.config(image=bg_photo)
    background_label.image = bg_photo


# Create the main window
window = tk.Tk()
window.title("Login Page of Attendence Software")

# Load and display a background image
bg_image = Image.open("background.jpg")  # Replace with your image file
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(window, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Set a larger window size
window.geometry("400x350")

# Increase font size for labels, entries, and button
font_style = ("Arial", 16)

# Create labels and entry widgets for login
username_label = tk.Label(window, text="Username:", font=font_style)
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

username_entry = tk.Entry(window, font=font_style)
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

password_label = tk.Label(window, text="Password:", font=font_style)
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

password_entry = tk.Entry(window, show="*", font=font_style)
password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

login_button = tk.Button(window, text="Login", command=login, font=font_style)
login_button.grid(row=2, columnspan=2, padx=10, pady=20)

forgot_password_button = tk.Button(
    window, text="Forgot Password", command=forgot_password, font=font_style
)
forgot_password_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Configure row and column weights for responsiveness
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Bind the resize event to the on_resize function
window.bind("<Configure>", on_resize)

# Start the main loop
window.mainloop()
