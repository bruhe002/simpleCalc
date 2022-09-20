from tkinter import *
from typing import Dict
# Use cases for Calculator


# Button functions
def clearPress(input: Entry):
    input.config(state='normal')
    input.delete(0, END)
    input.insert(0, '0')
    input.config(state='readonly')


def numPress(btnVal: int, input: Entry):
    input.config(state='normal')
    if input.get() == '0':
        input.delete(0, END)
    input.insert(END, str(btnVal))
    input.config(state='readonly')
    


def addPress(myDict: dict, input: Entry):
    myDict['operand'] = input.get()
    myDict['operator'] = '+'


def subPress(myDict: dict, input: Entry):
    myDict['operand'] = input.get()
    myDict['operator'] = '-'


def multPress(myDict: dict, input: Entry):
    myDict['operand'] = input.get()
    myDict['operator'] = 'X'


def divPress(myDict: dict, input: Entry):
    myDict['operand'] = input.get()
    myDict['operator'] = '/'

def decimalPress(input: Entry):
    input.config(state='normal')
    currentInput = input.get()
    # if currentInput == '0':
    #     input.delete(0, END)
    
    if not '.' in currentInput:
        input.insert(END, '.')
    
    input.config(state='readonly')


def equalsPress(myDict: dict, input: Entry):
    input.config(state='normal')
    operator = myDict['operator']
    operandOne = float(myDict['operand']) if '.' in myDict['operand'] else int(myDict['operand'])
    operandTwo = float(input.get()) if '.' in input.get() else int(input.get())

    value = 0

    if operator == '+':
        value = operandOne + operandTwo    
    elif operator == '-':
        value = operandOne - operandTwo
    elif operator == 'X':
        value = operandOne * operandTwo
    elif operator == '/':
        value = int(operandOne / operandTwo) if operandOne % operandTwo == 0 else float(operandOne / operandTwo)
    
    myDict['operand'] = str(value)

    input.delete(0, END)
    input.insert(0, str(value))

    input.config(state='readonly')


    

def signPress(input: Entry):
    input.config(state='normal')
    currentStr = input.get()
    if not currentStr == '0': 
        if not currentStr[0] == '-':
            input.insert(0, '-')
        else:
            input.delete(0, 1)
    
    input.config(state='readonly')

# # Logic Functions
# def changeOperation(opPhase: bool, secondInputPhase: bool):
#     pass


# def automaticOperation(opPhase: bool, secondInputPhase: bool):
#     pass