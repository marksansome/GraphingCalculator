#!/usr/bin/python
from Tkinter import *
from Modules.Output import graphing
from Modules.DataStructures import DocumentDictionary

import tkMessageBox
#constant width of each button (not)

'''
def generateList():				#USED FOR TESTING
	x = [];

	minX = float(minX)
	maxX = float(maxX)
	interval = float(interval)
	i = minX
	while(i <= maxX):
		x.append(i)
		i += interval
	return x
'''

def generateGraph(root, entry, minRange, maxRange, interval):

	DocumentDictionary.setUpperBound(maxRange)
	DocumentDictionary.setLowerBound(minRange)
	DocumentDictionary.setScale(interval)
	DocumentDictionary.setType(entry)
	#x = generateList()
	#y = [10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10]

	graphing.graph(root)
	return

def AddToEntry(entry, value):
	entry.insert(entry.index(INSERT), value)

#add value to entry box and put cursor in brackets
def AddToEntryBrackets(entry, value):
	entry.insert(entry.index(INSERT), value)
	entry.icursor(entry.index(INSERT)-1)

def UI():
	root = Tk()
	BUTTON_WIDTH = 5

	#lambda: parseString(entry.get())
	root.title('Name')
	frame = Frame(root)
	entryFrame = Frame(root)
	space = Frame(frame, width = 20, height = 4)
	entry = Entry(entryFrame, width = 40)
	minLabel = Label(entryFrame, text = "Min")
	minRange = Entry(entryFrame)
	minRange.insert(0, "-10")
	maxLabel = Label(entryFrame, text = "Max")
	maxRange = Entry(entryFrame)
	maxRange.insert(0, "10")
	interval = Spinbox(entryFrame, increment = 0.1, from_ = 0.1, to = 10)
	goButton = Button(entryFrame, text = "Go", command = lambda: generateGraph(root, entry.get(), minRange.get(), maxRange.get(), interval.get()))
	entryFrame.grid(row = 0, column = 0)
	entry.grid(row = 0 , column = 1, padx = 0)
	goButton.grid(row = 0, column = 0, padx = 0)
	interval.grid(row = 0, column = 2, padx = 0)
	minLabel.grid(row = 0, column = 3)
	minRange.grid(row = 0, column = 4)
	maxLabel.grid(row = 0, column = 5)
	maxRange.grid(row = 0, column = 6)
	entry.focus_set()

	num = [None]*10
	operator = [None]*100

#Create all number buttons with their values
	num[0] = Button(frame, text=0, width = 13, command = lambda: AddToEntry(entry,0))
	num[1] = Button(frame, text=1, width = BUTTON_WIDTH, command =lambda: AddToEntry(entry,1))
	num[2] = Button(frame, text=2, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,2))
	num[3] = Button(frame, text=3, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,3))
	num[4] = Button(frame, text=4, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,4))
	num[5] = Button(frame, text=5, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,5))
	num[6] = Button(frame, text=6, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,6))
	num[7] = Button(frame, text=7, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,7))
	num[8] = Button(frame, text=8, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,8))
	num[9] = Button(frame, text=9, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,9))

#create all operator buttons with thier values
	operator[0] = Button(frame, text='.', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"."))
#operator[1] = Button(frame, text='=', width = BUTTON_WIDTH)
	operator[2] = Button(frame, text='+', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"+"))
	operator[3] = Button(frame, text='-', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"-"))
	operator[4] = Button(frame, text='*', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"*"))
	operator[5] = Button(frame, text='/', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"/"))
	operator[6] = Button(frame, text='sin(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"sin()"))
	operator[7] = Button(frame, text='cos(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"cos()"))
	operator[8] = Button(frame, text='tan(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"tan()"))
	operator[9] = Button(frame, text='sinh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"sinh()"))
	operator[10] = Button(frame, text='cosh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"cosh()"))
	operator[11] = Button(frame, text='tanh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"tanh()"))
	operator[12] = Button(frame, text='arcsin(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arcsin()"))
	operator[13] = Button(frame, text='arccos(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arccos()"))
	operator[14] = Button(frame, text='arctan(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arctan()"))
	operator[15] = Button(frame, text='arcsinh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arcsinh()"))
	operator[16] = Button(frame, text='arccosh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arccosh()"))
	operator[17] = Button(frame, text='arctanh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arctanh()"))
	operator[18] = Button(frame, text='sqrt(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"sqrt()"))
	operator[19] = Button(frame, text='^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"^()"))
	operator[20] = Button(frame, text='1/x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"1/()"))
	operator[21] = Button(frame, text='10^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"10^()"))
	operator[22] = Button(frame, text='e^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"e^()"))
	operator[23] = Button(frame, text='pi', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"3.14"))
	operator[24] = Button(frame, text='!', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"!"))
	operator[25] = Button(frame, text='(y)Sqrt(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"()sqrt()"))
	operator[26] = Button(frame, text='logy(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"log()()"))
	operator[27] = Button(frame, text='en(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"en()"))

	#Initialize the frame grid
	frame.grid(row = 1)

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
	root.wm_title("Ranch Calc 2.0")

	root.mainloop()
