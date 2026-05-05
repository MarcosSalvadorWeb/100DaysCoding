import tkinter as tk

def calculate():
    try:
        miles_value = float(miles_input.get())
        km_value = miles_value * 1.60934
        result_label.config(text=f"{km_value:.2f}")
    except ValueError:
        result_label.config(text="Erro")

# Janela principal
window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(300, 100)
window.config(padx=20, pady=20)

# Input
miles_input = tk.Entry(width=10)
miles_input.grid(row=0, column=1)

# Labels
miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = tk.Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = tk.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

# Botão
calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()