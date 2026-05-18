# GUI Calculator using Tkinter
# A simple calculator with basic arithmetic operations

from tkinter import *
from tkinter import ttk

# Main window setup
window = Tk()
window.minsize(width=350, height=400)

# Input entry field
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    """Append number to the display"""
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Number buttons (0-9) - Created in a loop
x_positions = [10, 100, 190]
y_positions = [60, 120, 180, 240]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for idx, num in enumerate(numbers):
    row = idx // 3
    col = idx % 3
    b = ttk.Button(window, text=str(num), width=12, command=lambda n=num: click(n))
    b.place(x=x_positions[col], y=y_positions[row])

# Operator function
def set_operation(op):
    """Store first operand and set operation type"""
    global math, i
    math = op
    i = int(e.get())
    e.delete(0, END)

# Operator buttons - Created in a loop
operators = [
    ('+', 'addition', 100, 240),
    ('-', 'subtraction', 190, 240),
    ('*', 'multiplication', 10, 300),
    ('/', 'division', 100, 300)
]

for text, op, x, y in operators:
    b = ttk.Button(window, text=text, width=12, command=lambda o=op: set_operation(o))
    b.place(x=x, y=y)

# Equals function
def equal():
    """Evaluate the stored operation with both operands"""
    try:
        n2 = e.get()
        if not n2:
            e.insert(0, 'Error: Empty input')
            return
        n2 = int(n2)
        e.delete(0, END)
        if math == 'addition':
            e.insert(0, i + n2)
        elif math == 'subtraction':
            e.insert(0, i - n2)
        elif math == 'multiplication':
            e.insert(0, i * n2)
        elif math == 'division':
            if n2 == 0:
                e.insert(0, 'Error: Division by zero')
            else:
                result = i / n2
                e.insert(0, int(result) if result == int(result) else result)
    except ValueError:
        e.insert(0, 'Error: Invalid input')

b = ttk.Button(window, text='=', width=12, command=equal)
b.place(x=190, y=300)

# Clear function
def clear():
    """Clear the display"""
    e.delete(0, END)

b = ttk.Button(window, text='Clear', width=12, command=clear)
b.place(x=100, y=350)

# Start the GUI event loop
window.mainloop()