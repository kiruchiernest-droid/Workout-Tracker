import tkinter as tk
import math

# Create window
root = tk.Tk()
root.title("ERNEST CALCULATOR PRO")
root.geometry("320x420")

# Display screen
display = tk.Entry(root, width=20, font=("Arial", 22), borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, pady=10)

# Add number or symbol
def press(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

# Clear display
def clear():
    display.delete(0, tk.END)

# Calculate result
def equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Square root
def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

# Power (x²)
def power():
    try:
        result = float(display.get()) ** 2
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

# Buttons layout
buttons = [
('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

# Create number buttons
for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=6, height=2, command=equal)
    else:
        btn = tk.Button(root, text=text, width=6, height=2,
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Special buttons
tk.Button(root, text="C", width=6, height=2, command=clear).grid(row=5,column=0)
tk.Button(root, text="√", width=6, height=2, command=square_root).grid(row=5,column=1)
tk.Button(root, text="x²", width=6, height=2, command=power).grid(row=5,column=2)

# Exit button
tk.Button(root, text="Exit", width=6, height=2, command=root.quit).grid(row=5,column=3)

root.mainloop()