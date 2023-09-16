from tkinter import *
import os

# Create the root window
root = Tk()
root.title("Face Recognition Based Attendence System By Tech Tetris")
root.configure(background="white")

# Function to launch the attendance app
def function1():
    os.system("Logic.py")

# Function to exit the application
def function2():
    root.destroy()

# Function to open the GitHub page in a web browser
def open_github():
    import webbrowser
    webbrowser.open("https://github.com/SoumyaOk4-4/Face-Based-Attendence-SIH", new=2)

# Title Label
titleLabel = Label(
    root,
    text="Face Recognition Based Attendance System",
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
copyrightLabel.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 10))  # Adjusted the bottom pady

# Create a beautiful hyperlink
githubLink = Label(
    root,
    text="GitHub Source Code",
    font=("Arial", 10, "underline"),
    fg="#007acc",  # Blue color
    bg="white",
    cursor="hand2",
)
githubLink.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20))  # Adjusted the top pady
githubLink.bind("<Button-1>", lambda event: open_github())

# Give Attendance Button
attendanceButton = Button(
    root,
    text="Give Attendance",
    font=("Arial", 18),
    bg="#007acc",
    fg="white",
    command=function1,
)
attendanceButton.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Exit Button
exitButton = Button(
    root,
    text="Exit",
    font=("Arial", 18),
    bg="#cc0000",
    fg="white",
    command=function2,
)
exitButton.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

# Configure row and column weights to make the UI elements expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the main loop
root.mainloop()
