from tkinter import *
import os

# Create the root window
root = Tk()
root.title("Facial Recognition Attendance System")
root.configure(background="white")

# Function to launch the attendance app
def function1():
    os.system("Logic.py")

# Function to exit the application
def function2():
    root.destroy()

# Title Label
titleLabel = Label(
    root,
    text="Face Recognition-Based Attendance System",
    font=("Arial", 24, "bold"),
    fg="black",
    bg="white",
)
titleLabel.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))

# Copyright Label
copyrightLabel = Label(
    root,
    text="Copyright © 2023 Tech Tetris",
    font=("Arial", 10),
    fg="gray",
    bg="white",
)
copyrightLabel.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20))

# Give Attendance Button
attendanceButton = Button(
    root,
    text="Give Attendance",
    font=("Arial", 18),
    bg="#007acc",
    fg="white",
    command=function1,
)
attendanceButton.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Exit Button
exitButton = Button(
    root,
    text="Exit",
    font=("Arial", 18),
    bg="#cc0000",
    fg="white",
    command=function2,
)
exitButton.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Configure row and column weights to make the UI elements expandable
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the main loop
root.mainloop()