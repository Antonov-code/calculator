from tkinter import messagebox
import tkinter as tk
from tkinter.constants import DISABLED, RIGHT


def add_digit(digit):
    value = calc.get()
    try:
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
    except IndexError:
        calc.insert(0, '0')
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Error', 'Its a calculator, it doesn\'t count string!')
        calc.insert(0, '0')

def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def make_digit_button(digit):
    return tk.Button(text=f'{digit}', bd=6, font=('Arial', 20), command= lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=f'{operation}', bd=6, font=('Arial', 20), command= lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=f'{operation}', bd=6, font=('Arial', 20), command=calculate)

def make_clear_button(operation):
    return tk.Button(text=f'{operation}', bd=6, font=('Arial', 20), command=clear)

def press_key(event):
    # if event.char.isdigit():
    #     add_digit(event.char)
    if event.char in '+-*/':
        add_operation(event.char)
    if event.char in '=' or event.char == '\r':
        calculate()



root = tk.Tk()
root.geometry('240x305')
root.resizable(width=False, height=False)
root.title('calculator')
root.bind('<Key>', press_key)

calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 24), width=12, relief=tk.RAISED, bd=6)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we')

make_digit_button('0').grid(row=4, column=1, stick='nesw') #, padx=2, pady=2
make_digit_button('1').grid(row=3, column=0, stick='nesw')
make_digit_button('2').grid(row=3, column=1, stick='nesw')
make_digit_button('3').grid(row=3, column=2, stick='nesw')
make_digit_button('4').grid(row=2, column=0, stick='nesw')
make_digit_button('5').grid(row=2, column=1, stick='nesw')
make_digit_button('6').grid(row=2, column=2, stick='nesw')
make_digit_button('7').grid(row=1, column=0, stick='nesw')
make_digit_button('8').grid(row=1, column=1, stick='nesw')
make_digit_button('9').grid(row=1, column=2, stick='nesw')

make_operation_button('+').grid(row=1, column=3, stick='nesw')
make_operation_button('-').grid(row=2, column=3, stick='nesw')
make_operation_button('/').grid(row=3, column=3, stick='nesw')
make_operation_button('*').grid(row=4, column=3, stick='nesw')

make_calc_button('=').grid(row=4, column=2, stick='nesw')

make_clear_button('C').grid(row=4, column=0, stick='nesw')



root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.rowconfigure(1, minsize=60)
root.rowconfigure(2, minsize=60)
root.rowconfigure(3, minsize=60)
root.rowconfigure(4, minsize=60)




root.mainloop()










