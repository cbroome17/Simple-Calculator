from tkinter import *

#Lambda allows us to pass parameter through butotn function
#58:27
root = Tk()
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, ipady=15) #padx=10, pady=10

adding = False

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return 

def clear_():
    e.delete(0, END)
    return

def button_add(): 
    first_number = e.get()
    global f_num
    global math
    math = 'adding'
    f_num = int(first_number)
    e.delete(0, END)
def button_minus(): 
    first_number = e.get()
    global f_num
    global math
    math = 'subtract'
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply(): 
    first_number = e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0, END)
def button_divide(): 
    first_number = e.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'adding':
        e.insert(0, f_num + int(second_number))
    elif math == 'subtract':
        e.insert(0, f_num - int(second_number))
    elif math == 'multiply':
        e.insert(0, f_num * int(second_number))
    elif math == 'divide':
        e.insert(0, f_num / int(second_number))

def clear_all():
    e.delete(0, END)
    global f_num
    f_num = 0

button_1 = Button(root, text=1 , command=lambda: button_click(1), width=8, borderwidth=5, pady=30)
button_1.grid(row=1,column=0,columnspan=1)

button_2 = Button(root, text=2, width=8, borderwidth=5, pady=30, command=lambda: button_click(2))
button_2.grid(row=1,column=1,columnspan=1)

button_3 = Button(root, text=3, width=8, borderwidth=5, pady=30, command=lambda: button_click(3))
button_3.grid(row=1,column=2,columnspan=1)

button_4 = Button(root, text=4, width=8, borderwidth=5, pady=30, command=lambda: button_click(4))
button_4.grid(row=2,column=0,columnspan=1)

button_5 = Button(root, text=5, width=8, borderwidth=5, pady=30, command=lambda: button_click(5))
button_5.grid(row=2,column=1,columnspan=1)

button_6 = Button(root, text=6, width=8, borderwidth=5, pady=30, command=lambda: button_click(6))
button_6.grid(row=2,column=2,columnspan=1)

button_7 = Button(root, text=7, width=8, borderwidth=5, pady=30, command=lambda: button_click(7))
button_7.grid(row=3,column=0,columnspan=1)

button_8 = Button(root, text=8, width=8, borderwidth=5, pady=30, command=lambda: button_click(8))
button_8.grid(row=3,column=1,columnspan=1)

button_9 = Button(root, text=9, width=8, borderwidth=5, pady=30, command=lambda: button_click(9))
button_9.grid(row=3,column=2,columnspan=1)

button_0 = Button(root, text=0, width=8, borderwidth=5, pady=30, command=lambda: button_click(0))
button_0.grid(row=4,column=0,columnspan=1)

button_add = Button(root, text='+', width=8, pady=30, command=button_add)
button_add.grid(row=4,column=1,columnspan=1)

button_minus = Button(root, text='-', width=8, pady=30, command=button_minus)
button_minus.grid(row=4, column=2, columnspan=1)

button_asterik = Button(root, text='*', width=8, pady=30, command=button_multiply)
button_asterik.grid(row=5,column=0, columnspan=1)

button_slash = Button(root, text='/', width=8, pady=30, command=button_divide)
button_slash.grid(row=5, column=1, columnspan=1)

button_equal = Button(root, text='=', width=8, pady=30, command=button_equal)
button_equal.grid(row=5, column=2, columnspan=1)

button_clear = Button(root, text='CLEAR', width=35, command=lambda: clear_())
button_clear.grid(row=6, column=0, columnspan=3)

button_clearMASTER = Button(root, text='CLEAR/ALL', width=35, command=clear_all)
button_clearMASTER.grid(row=7, column=0, columnspan=3)

root.mainloop()