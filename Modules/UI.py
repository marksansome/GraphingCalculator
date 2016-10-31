#!/usr/bin/python
from Tkinter import *

import tkMessageBox
#constant width of each button (not)
BUTTON_WIDTH = 5

#add value to entry box 
def AddToEntry(value):
	entry.insert(entry.index(INSERT), value)

#add value to entry box and put cursor in brackets
def AddToEntryBrackets(value):
	entry.insert(entry.index(INSERT), value)
	entry.icursor(entry.index(INSERT)-1)

root = Tk()


root.title('Name')
frame = Frame(root)
space = Frame(frame, width = 20, height = 4)
entry = Entry(root, width = 80)
goButton = Button(root, text = "Go")
entry.grid(row = 0 , column = 0, padx = 0)
goButton.grid(row = 0, column = 0, padx = 0)
entry.focus_set()
num = [None]*10
operator = [None]*100

#Create all number buttons with their values
num[0] = Button(frame, text=0, width = 13, command = lambda: AddToEntry(0))
num[1] = Button(frame, text=1, width = BUTTON_WIDTH, command =lambda: AddToEntry(1))
num[2] = Button(frame, text=2, width = BUTTON_WIDTH, command = lambda: AddToEntry(2))
num[3] = Button(frame, text=3, width = BUTTON_WIDTH, command = lambda: AddToEntry(3))
num[4] = Button(frame, text=4, width = BUTTON_WIDTH, command = lambda: AddToEntry(4))
num[5] = Button(frame, text=5, width = BUTTON_WIDTH, command = lambda: AddToEntry(5))
num[6] = Button(frame, text=6, width = BUTTON_WIDTH, command = lambda: AddToEntry(6))
num[7] = Button(frame, text=7, width = BUTTON_WIDTH, command = lambda: AddToEntry(7))
num[8] = Button(frame, text=8, width = BUTTON_WIDTH, command = lambda: AddToEntry(8))
num[9] = Button(frame, text=9, width = BUTTON_WIDTH, command = lambda: AddToEntry(9))

#create all operator buttons with thier values
operator[0] = Button(frame, text='.', width = BUTTON_WIDTH, command = lambda: AddToEntry("."))
#operator[1] = Button(frame, text='=', width = BUTTON_WIDTH)
operator[2] = Button(frame, text='+', width = BUTTON_WIDTH, command = lambda: AddToEntry("+"))
operator[3] = Button(frame, text='-', width = BUTTON_WIDTH, command = lambda: AddToEntry("-"))
operator[4] = Button(frame, text='*', width = BUTTON_WIDTH, command = lambda: AddToEntry("*"))
operator[5] = Button(frame, text='/', width = BUTTON_WIDTH, command = lambda: AddToEntry("/"))
operator[6] = Button(frame, text='sin(x)', width = 10, command = lambda: AddToEntryBrackets("sin()"))
operator[7] = Button(frame, text='cos(x)', width = 10, command = lambda: AddToEntryBrackets("cos()"))
operator[8] = Button(frame, text='tan(x)', width = 10, command = lambda: AddToEntryBrackets("tan()"))
operator[9] = Button(frame, text='sinh(x)', width = 10, command = lambda: AddToEntryBrackets("sinh()"))
operator[10] = Button(frame, text='cosh(x)', width = 10, command = lambda: AddToEntryBrackets("cosh()"))
operator[11] = Button(frame, text='tanh(x)', width = 10, command = lambda: AddToEntryBrackets("tanh()"))
operator[12] = Button(frame, text='arcsin(x)', width = 10, command = lambda: AddToEntryBrackets("arcsin()"))
operator[13] = Button(frame, text='arccos(x)', width = 10, command = lambda: AddToEntryBrackets("arccos()"))
operator[14] = Button(frame, text='arctan(x)', width = 10, command = lambda: AddToEntryBrackets("arctan()"))
operator[15] = Button(frame, text='arcsinh(x)', width = 10, command = lambda: AddToEntryBrackets("arcsinh()"))
operator[16] = Button(frame, text='arccosh(x)', width = 10, command = lambda: AddToEntryBrackets("arccosh()"))
operator[17] = Button(frame, text='arctanh(x)', width = 10, command = lambda: AddToEntryBrackets("arctanh()"))
operator[18] = Button(frame, text='sqrt(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("sqrt()"))
operator[19] = Button(frame, text='^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("^()"))
operator[20] = Button(frame, text='1/x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("1/()"))
operator[21] = Button(frame, text='10^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("10^()"))
operator[22] = Button(frame, text='e^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("e^()"))
operator[23] = Button(frame, text='pi', width = BUTTON_WIDTH, command = lambda: AddToEntry("3.14"))
operator[24] = Button(frame, text='!', width = BUTTON_WIDTH, command = lambda: AddToEntry("!"))
operator[25] = Button(frame, text='(y)Sqrt(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("()sqrt()"))
operator[26] = Button(frame, text='logy(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("log()()"))
operator[27] = Button(frame, text='en(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets("en()"))

#Initialize the frame grid
frame.grid()

#initialize each button in the frame in their respective rows and columns
space.grid(row = 0 , column = 4)
num[1].grid(row = 0, column = 0)
num[2].grid(row = 0, column = 1)
num[3].grid(row = 0, column = 2)
num[4].grid(row = 1, column = 0)
num[5].grid(row = 1, column = 1)
num[6].grid(row = 1, column = 2)
num[7].grid(row = 2, column = 0)
num[8].grid(row = 2, column = 1)
num[9].grid(row = 2, column = 2)
num[0].grid(row = 3, column = 1, columnspan = 2)
operator[0].grid(row = 3, column = 0)
#operator[1].grid(row = 3, column = 2)
operator[2].grid(row = 0,column = 3)
operator[3].grid(row = 1,column = 3)
operator[4].grid(row = 2,column = 3)
operator[5].grid(row = 3,column = 3)
operator[6].grid(row = 0,column = 5)
operator[7].grid(row = 1,column = 5)
operator[8].grid(row = 2,column = 5)
operator[9].grid(row = 3,column = 5)
operator[10].grid(row = 0,column = 6)
operator[11].grid(row = 1,column = 6)
operator[12].grid(row = 2,column = 6)
operator[13].grid(row = 3,column = 6)
operator[14].grid(row = 0,column = 7)
operator[15].grid(row = 1,column = 7)
operator[16].grid(row = 2,column = 7)
operator[17].grid(row = 3,column = 7)
operator[18].grid(row = 0,column = 8)
operator[19].grid(row = 1,column = 8)
operator[20].grid(row = 2,column = 8)
operator[21].grid(row = 3,column = 8)
operator[22].grid(row = 0,column = 9)
operator[23].grid(row = 1,column = 9)
operator[24].grid(row = 2,column = 9)
operator[25].grid(row = 3,column = 9)
operator[26].grid(row = 0,column = 10)
operator[27].grid(row = 1,column = 10)

root.mainloop()



