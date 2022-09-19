from tkinter import *

rootWindow = Tk()


# Create margins for window
rootWindow.geometry('332x450')
rootWindow.resizable(False, False)

# row 0
clearBtn = Button(rootWindow, text='C', font='18', padx=29, pady=30).grid(row=0, column=0)
entry = Entry(rootWindow, font=('Ariel',16), borderwidth=5).grid(row=0, column=1, columnspan=3)

# row 1
sevenBtn = Button(rootWindow, text='7', font='20', padx=31, pady=30).grid(row=1,column=0)
eightBtn = Button(rootWindow, text='8', font='20', padx=31, pady=30).grid(row=1,column=1)
nineBtn = Button(rootWindow, text='9', font='20', padx=31, pady=30).grid(row=1,column=2)
addBtn = Button(rootWindow, text='+', font='20', padx=31, pady=30, bg='#D3D3D3').grid(row=1,column=3)

# row 2
fourBtn = Button(rootWindow, text='4', font='20', padx=31, pady=30).grid(row=2,column=0)
fiveBtn = Button(rootWindow, text='5', font='20', padx=31, pady=30).grid(row=2,column=1)
sixBtn = Button(rootWindow, text='6', font='20', padx=31, pady=30).grid(row=2,column=2)
subBtn = Button(rootWindow, text='-', font='30', padx=33, pady=30, bg='#D3D3D3').grid(row=2,column=3)

# row 3
oneBtn = Button(rootWindow, text='1', font='20', padx=31, pady=30).grid(row=3,column=0)
twoBtn = Button(rootWindow, text='2', font='20', padx=31, pady=30).grid(row=3,column=1)
threeBtn = Button(rootWindow, text='3', font='20', padx=31, pady=30).grid(row=3,column=2)
multBtn = Button(rootWindow, text='X', font='20', padx=30, pady=30, bg='#D3D3D3').grid(row=3,column=3)

# row 4
decimalBtn = Button(rootWindow, text='.00', font='19', padx=24, pady=30, bg='#D3D3D3').grid(row=4,column=0)
zeroBtn = Button(rootWindow, text='0', font='20', padx=31, pady=30).grid(row=4,column=1)
equalBtn = Button(rootWindow, text='=', font='20', padx=31, pady=30, bg='#D3D3D3').grid(row=4,column=2)
divBtn = Button(rootWindow, text='/', font='21', padx=33, pady=30, bg='#D3D3D3').grid(row=4,column=3)

rootWindow.mainloop()