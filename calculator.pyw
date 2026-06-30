import tkinter as tk

window = tk.Tk()
window.title("My Calculator 🔥")
window.geometry("320x450")
window.configure(bg="#1E1E1E")  # тёмный фон
window.resizable(False, False)

# ---------- функции ----------

def press(symbol):
    entry.insert(tk.END, symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# ---------- экран ----------

entry = tk.Entry(
    window,
    font=("Arial", 26),
    bg="#2C2C2C",
    fg="white",
    justify="right",
    bd=0
)

entry.place(x=10, y=20, width=300, height=60)

# ---------- кнопки ----------

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]

x = 10
y = 100

for b in buttons:

    if b == "=":
        cmd = calculate
        color = "#FF8C42"  # оранжевая
    elif b == "C":
        cmd = clear
        color = "#34C759"  # зелёная
    else:
        cmd = lambda x=b: press(x)
        color = "#3A3A3A"

    tk.Button(
        window,
        text=b,
        command=cmd,
        font=("Arial", 18, "bold"),
        bg=color,
        fg="white",
        bd=0,
        activebackground="#555555"
    ).place(x=x, y=y, width=65, height=65)

    x += 75

    if x > 235:
        x = 10
        y += 75

window.mainloop()
