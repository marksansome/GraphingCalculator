#!/usr/bin/python
from Tkinter import *

import tkMessageBox

root = Tk()

def printtext():
    global e
    string = e.get() 
    print string   

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
d = Button(root, text='hello')
e = Button(root, text='world')
d.pack(side=LEFT)
e.pack(side=LEFT)
b.pack(side='bottom')
root.mainloop()