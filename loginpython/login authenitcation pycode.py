import tkinter as tk
from tkinter import messagebox

def validate_login(username, password):

    #   using coded values
    valid_username = "oasisinfobyte"
    valid_password = "password"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def on_login_button_click():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if validate_login(entered_username, entered_password):
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# main window
root = tk.Tk()
root.title("Login Authentication")
root.geometry("400x300")
root.config(bg="#CAFF70")  # Set background color

# Create a frame for the login page
login_frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=5, relief=tk.GROOVE)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Page heading
heading_label = tk.Label(root, text="OASIS INFOBYTE", font=("Helvetica", 20, "bold"), bg="#98F5FF", fg="darkgreen")
heading_label.pack(pady=10)

# Create  stylings
label_username = tk.Label(login_frame, text="Username:", font=("Helvetica", 12), bg="white")
username_entry = tk.Entry(login_frame, font=("Helvetica", 12))

label_password = tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg="white")
password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))

login_button = tk.Button(login_frame, text="Login", command=on_login_button_click, font=("Helvetica", 12), bg="#2ecc71", fg="white")

# Arrange layouts
label_username.grid(row=0, column=0, sticky=tk.E, pady=5)
username_entry.grid(row=0, column=1, pady=5)

label_password.grid(row=1, column=0, sticky=tk.E, pady=5)
password_entry.grid(row=1, column=1, pady=5)

login_button.grid(row=2, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()




