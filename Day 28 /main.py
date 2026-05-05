import math
import tkinter as tk
from PIL.PngImagePlugin import PngImageFile

#---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    check_mark.config(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    time_format = f"{count_min:02d}:{count_sec:02d}"
    canvas.itemconfig(timer_text, text=time_format)
    if count > 0:
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        mark = ""
        ct = 0
        for i in range(math.floor(reps/2)):
            mark += "✔"
            ct += ct
        check_mark.config(text=mark, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
        with open("./data.txt", "w") as file:
            file.write(ct)

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=200, pady=100, background=YELLOW)

# Label
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=2)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=2)

# Botões
start_button = tk.Button(text="Start", bg=YELLOW, command=start_timer,highlightthickness=0)
start_button.grid(row=2, column=1)

reset_button = tk.Button(text="Reset", bg=YELLOW, command=reset,highlightthickness=0)
reset_button.grid(row=2, column=3)

check_mark = tk.Label(text = "", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check_mark.grid(row=3, column=2)

with open("data.txt", "r") as file:
    file_content = file.read()

data = tk.Label(text=f"Record: {file_content}", font=(FONT_NAME, 12, "italic"), bg=YELLOW)
data.grid(row=7, column=2)

window.mainloop()