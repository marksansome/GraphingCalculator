#!/usr/bin/python
from Tkinter import *

import tkMessageBox

root = Tk()

def printtext():
    global e
    string = e.get() 
    print string   

root.title('Name')
frame = Frame(root)
e = Entry(root, width = 40)
e.grid()
e.focus_set()
num = [None]*10
for i in range(0,10):
	num[i] = Button(frame, text=i)

frame.grid()

num[1].grid(row=0, column = 0)
num[2].grid(row=0, column = 1)
num[3].grid(row=0, column = 2)
num[4].grid(row=1, column = 0)
num[5].grid(row=1, column = 1)
num[6].grid(row=1, column = 2)
num[7].grid(row=2, column = 0)
num[8].grid(row=2, column = 1)
num[9].grid(row=2, column = 2)
num[0].grid(row=3, column = 1)
root.mainloop()