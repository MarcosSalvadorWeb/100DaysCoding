# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import messagebox
import pyperclip
from passgen import generate_password

def generate():
    password = generate_password()
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    if web != "" and user != "" and password != "":
        data = f"{web} | {user} | {password} \n"

        is_ok = messagebox.askokcancel(title="Save", message=f"Attention to the details \n Email:{user} \n Password:{password} \n Its okay to save? ")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(data)
                website_entry.delete(0, "end")
                username_entry.delete(0, "end")
                password_entry.delete(0, "end")
    else:
        messagebox.showerror(title="Error", message="Please fill all the fields")

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ================= IMAGEM =================
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
image = tk.PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# ================= WEBSITE =================
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0 )

website_entry = tk.Entry(width=40)
website_entry.grid(row=1, column=1,columnspan=2)

# ================= USERNAME =================
username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = tk.Entry(width=40)
username_entry.grid(row=2, column=1,columnspan=2)
username_entry.insert(0,"salvadormarcosjr@usp.br")
# ================= PASSWORD =================
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# ================= BUTTON ==================
generate_button = tk.Button(
    text="Generate Password",
    highlightthickness=0, command=generate)

generate_button.grid(row=3, column=2)

add_button = tk.Button(
    text="Add",
    width=36, command=save
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
