# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import messagebox
import pyperclip
from passgen import generate_password
import json

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

    new_data = {web: {
        "username": user,
        "password": password}}


    if len(web) != 0 and len(user) != 0 and len(password) != 0:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
    else:
        messagebox.showerror(title="Error", message="Please fill all the fields")

def find_password():
    web = website_entry.get()
    with open("data.json","r") as data_file:
        data = json.load(data_file)
        if web in data:
            email = data[web]["username"]
            password = data[web]["password"]
            messagebox.showinfo(title= web, message= f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)

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

website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)

# ================= USERNAME =================
username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = tk.Entry(width=39)
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

search_button = tk.Button(text="Search", command=find_password,width=13)
search_button.grid(row=1, column=2)

window.mainloop()
