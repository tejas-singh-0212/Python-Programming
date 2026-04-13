# GUI Calculator using Tkinter
# A simple calculator with basic arithmetic operations

from tkinter import *
from tkinter import ttk

# Main window setup
window = Tk()
window.minsize(width=500, height=500)

# Input entry field
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    """Append number to the display"""
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Number buttons (0-9)
b = ttk.Button(window, text='1', width=12, command=lambda: click(1))
b.place(x=10, y=60)

b = ttk.Button(window, text='2', width=12, command=lambda: click(2))
b.place(x=80, y=60)

b = ttk.Button(window, text='3', width=12, command=lambda: click(3))
b.place(x=170, y=60)

b = ttk.Button(window, text='4', width=12, command=lambda: click(4))
b.place(x=10, y=120)

b = ttk.Button(window, text='5', width=12, command=lambda: click(5))
b.place(x=80, y=120)

b = ttk.Button(window, text='6', width=12, command=lambda: click(6))
b.place(x=170, y=120)

b = ttk.Button(window, text='7', width=12, command=lambda: click(7))
b.place(x=10, y=180)

b = ttk.Button(window, text='8', width=12, command=lambda: click(8))
b.place(x=80, y=180)

b = ttk.Button(window, text='9', width=12, command=lambda: click(9))
b.place(x=170, y=180)

b = ttk.Button(window, text='0', width=12, command=lambda: click(0))
b.place(x=10, y=240)

# Operator functions (+, -, *, /)
def add():
    """Store first operand and set operation to addition"""
    n1=e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)

b = ttk.Button(window, text='+', width=12, command=add)
b.place(x=80, y=240)

def subtract():
    """Store first operand and set operation to subtraction"""
    global math
    math = 'subtraction'
    n1=e.get()
    global i
    i = int(n1)
    e.delete(0, END)

b = ttk.Button(window, text='-', width=12, command=subtract)
b.place(x=170, y=240)

def multiply():
    """Store first operand and set operation to multiplication"""
    global math
    math = 'multiplication'
    n1=e.get()
    global i
    i = int(n1)
    e.delete(0, END)


b = ttk.Button(window, text='*', width=12, command=multiply)
b.place(x=10, y=300)

def divide():
    """Store first operand and set operation to division"""
    global math
    math = 'division'
    n1=e.get()
    global i
    i = int(n1)
    e.delete(0, END)

b = ttk.Button(window, text='/', width=12, command=divide)
b.place(x=80, y=300)

# Equals function
def equal():
    """Evaluate the stored operation with both operands"""
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, i + int(n2))
    elif math == 'subtraction':
        e.insert(0, i - int(n2))
    elif math == 'multiplication':
        e.insert(0, i * int(n2))
    elif math == 'division':
        if n2 == '0' or n2 == '0.0':
            e.insert(0, 'Error: Division by zero')
        else:
            e.insert(0, i / int(n2))

b = ttk.Button(window, text='=', width=12, command=equal)
b.place(x=170, y=300)

# Clear function
def clear():
    """Clear the display"""
    e.delete(0, END)

b = ttk.Button(window, text='Clear', width=12, command=clear)
b.place(x=10, y=350)

# Start the GUI event loop
window.mainloop()