BACKGROUND_COLOR = "#B1DDC6"

#-------------------------------WORD------------------------------------#
import pandas as pd
import random as rnd
current_word = {}
to_learn = {}
try:
    data_learned = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pd.read_csv("data/french_words.csv")
    to_learn = french_words.to_dict(orient="records")
else:
    to_learn = data_learned.to_dict(orient="records")

def change_words():
    global current_word,flip_timer
    window.after_cancel(flip_timer)
    current_word = rnd.choice(to_learn)
    canvas.itemconfig(card_word, text = current_word["French"], fill = "Black")
    canvas.itemconfig(card_title, text = "French", fill = "Black")
    canvas.itemconfig(card_background, image = front)
    window.after(4000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English",fill = "white")
    canvas.itemconfig(card_word, text = current_word["English"], fill = "white")
    canvas.itemconfig(card_background, image = back)

def is_known():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    change_words()

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk

window = tk.Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50,background=BACKGROUND_COLOR)
flip_timer = window.after(4000, flip_card)

canvas = tk.Canvas(width=800, height=526)
back = tk.PhotoImage(file="./images/card_back.png")
front = tk.PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400,263, image=front)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text ="Word", font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

right = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(image=right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

wrong = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=wrong, highlightthickness=0, command=change_words)
button_wrong.grid(row=1, column=0)

change_words()
window.mainloop()