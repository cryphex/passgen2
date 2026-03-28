import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import string
import os
import sys


# pyinstaller
def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS  # type: ignore
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


# passgen
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("PassGen2 - Error", "Please enter a valid positive integer")
        return

    chars = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + '!"§$%&()=?-_.,:;<+*#>@€{}[]|'
    )

    password = "".join(random.choice(chars) for _ in range(length))
    output_var.set(password)


def copy_password():
    if output_var.get():
        pyperclip.copy(output_var.get())
        messagebox.showinfo(
            "PassGen2 - Success",
            "Successfully copied the password into the clipboard!",
        )
    else:
        messagebox.showwarning(
            "PassGen2 - Warning",
            "Nothing to copy! Generate the password first by clicking 'Generate Password'.",
        )


# gui
root = tk.Tk()
root.title("PassGen2")
root.geometry("450x250")

# window icon
icon_path = resource_path("favicon.png")
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon)

# window
window_width = 450
window_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)

# input
tk.Label(root, text="Enter total Password characters:", font=("Arial", 10)).pack(
    pady=10
)
entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
entry.pack(pady=5)
entry.insert(0, "12")

# output
output_var = tk.StringVar()
tk.Label(root, text="Generated Password:", font=("Arial", 10)).pack(pady=(20, 5))
output_entry = tk.Entry(
    root,
    textvariable=output_var,
    font=("Arial", 12),
    width=35,
    state="readonly",
    bg="white",
)
output_entry.pack(pady=5)

# buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=30)

gen_btn = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18,
    height=2,
    relief="raised",
    bd=4,
    cursor="hand2",
)
gen_btn.pack(side=tk.LEFT, padx=15)  # type: ignore

copy_btn = tk.Button(
    button_frame,
    text="Copy Output",
    command=copy_password,
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=14,
    height=2,
    relief="raised",
    bd=4,
    cursor="hand2",
)
copy_btn.pack(side=tk.LEFT, padx=15)  # type: ignore

root.mainloop()
