from tkinter import *

rootWindow = Tk()


# Create margins for window
rootWindow.geometry('332x520')
rootWindow.resizable(False, False)

# row 0
clearBtn = Button(rootWindow, text='C', font='18', bg='#CC3E3E', padx=29, pady=30)
clearBtn.grid(row=0, column=0)

entry = Entry(rootWindow, font=('Ariel',16), borderwidth=5)
entry.grid(row=0, column=1, columnspan=3)
entry.insert(0, "0")
entry.config(state= "disabled")

# row 1
sevenBtn = Button(rootWindow, text='7', font='20', padx=31, pady=30)
sevenBtn.grid(row=1,column=0)

eightBtn = Button(rootWindow, text='8', font='20', padx=31, pady=30)
eightBtn.grid(row=1,column=1)

nineBtn = Button(rootWindow, text='9', font='20', padx=31, pady=30)
nineBtn.grid(row=1,column=2)

addBtn = Button(rootWindow, text='+', font='20', padx=31, pady=30, bg='#D3D3D3')
addBtn.grid(row=1,column=3)

# row 2
fourBtn = Button(rootWindow, text='4', font='20', padx=31, pady=30)
fourBtn.grid(row=2,column=0)

fiveBtn = Button(rootWindow, text='5', font='20', padx=31, pady=30)
fiveBtn.grid(row=2,column=1)

sixBtn = Button(rootWindow, text='6', font='20', padx=31, pady=30)
sixBtn.grid(row=2,column=2)

subBtn = Button(rootWindow, text='-', font='30', padx=33, pady=30, bg='#D3D3D3')
subBtn.grid(row=2,column=3)

# row 3
oneBtn = Button(rootWindow, text='1', font='20', padx=31, pady=30)
oneBtn.grid(row=3,column=0)

twoBtn = Button(rootWindow, text='2', font='20', padx=31, pady=30)
twoBtn.grid(row=3,column=1)

threeBtn = Button(rootWindow, text='3', font='20', padx=31, pady=30)
threeBtn.grid(row=3,column=2)

multBtn = Button(rootWindow, text='X', font='20', padx=30, pady=30, bg='#D3D3D3')
multBtn.grid(row=3,column=3)

# row 4
decimalBtn = Button(rootWindow, text='.00', font='19', padx=24, pady=30, bg='#D3D3D3')
decimalBtn.grid(row=4,column=0)

zeroBtn = Button(rootWindow, text='0', font='20', padx=31, pady=30)
zeroBtn.grid(row=4,column=1)

equalBtn = Button(rootWindow, text='=', font='20', padx=31, pady=30, bg='#D3D3D3')
equalBtn.grid(row=4,column=2)

divBtn = Button(rootWindow, text='/', font='21', padx=33, pady=30, bg='#D3D3D3')
divBtn.grid(row=4,column=3)

# row 5
signBtn = Button(rootWindow, text="+ / -", font='30', padx=150, pady=20, bg='#D3D3D3')
signBtn.grid(row=5, column=0, columnspan=4)

rootWindow.mainloop()