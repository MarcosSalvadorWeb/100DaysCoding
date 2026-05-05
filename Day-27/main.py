import tkinter as tk

# Creating a Window
window = tk.Tk()
window.title("My First GUI")
window.minsize(500, 300)

# Creating a Label
my_label = tk.Label(window, text="Wow, so cool", font=("Arial", 12,"italic"))
my_label.grid(row=0, column=1)


# Creating a Button
def button_clicked():
    my_label["text"] = "Button Clicked"
    my_label["text"] = input.get()

button = tk.Button(text="Click me!", command=button_clicked)
button.grid(row=1, column=2)

# Creating a Input
input = tk.Entry(width=40)
input.grid(row=2, column=2)

# Text BOX
text = tk.Text(height=5,width=20)
text.focus()
text.insert("1.0", "Hello World")
text.grid(row=3, column=3)


window.mainloop()