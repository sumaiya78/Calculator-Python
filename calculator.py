import tkinter as tk
import math

# Main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry box
entry = tk.Entry(root, width=30, font=("Arial", 16), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=5, pady=10)

# Button click function
def button_click(symbol):
    entry.insert(tk.END, symbol)

# Clear function
def clear():
    entry.delete(0, tk.END)

# Calculate function
def calculate():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, math.__dict__)  # নিরাপদ eval
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ["7", "8", "9", "/", "sin"],
    ["4", "5", "6", "*", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "(", ")", "+"],
    ["sqrt", "log", "pi", "exp", "="],
]

# Create buttons
for r, row in enumerate(buttons, start=1):
    for c, symbol in enumerate(row):
        if symbol == "=":
            btn = tk.Button(root, text=symbol, width=6, height=2,
                            command=calculate, font=("Arial", 14))
        else:
            btn = tk.Button(root, text=symbol, width=6, height=2,
                            command=lambda s=symbol: button_click(s), font=("Arial", 14))
        btn.grid(row=r, column=c, padx=2, pady=2)

# Clear button
btn_clear = tk.Button(root, text="C", width=32, height=2, command=clear, font=("Arial", 14))
btn_clear.grid(row=6, column=0, columnspan=5, pady=5)

root.mainloop()
