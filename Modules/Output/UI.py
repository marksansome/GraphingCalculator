#!/usr/bin/python
from Tkinter import *
from Modules.Output import graphing
from Modules.DataStructures import DocumentDictionary
from Modules.Input.Verifier import *
from Modules.Maths.FillTree import *

import tkFont
import tkMessageBox


def generateGraph(op, var, root, entry, minRange, maxRange, interval):
	if checkRanges(minRange, maxRange): 

def saveSettings(mode):
	fpt = open('settings.txt', 'w')
	fpt.write("mode=" + mode + "\n")
	fpt.close()

def configureSettings():
	SETTINGS = []
	fpt = open('settings.txt', 'r')
	dataFile = fpt.read()
	SETTINGS = dataFile.split('\n')
	fpt.close()
	window = Tk()
	window.title("Settings")
	window.configure(background = "#f2f2f2")
	frame = Frame(window, bg="#f2f2f2", height=400, width=300)
	frame.pack()
	#save/exit  button
	saveButton = Button(frame, text = "Save", command = lambda: saveSettings(angleVar.get()))
	saveButton.grid(row = 0, column = 0)
	exitButton = Button(frame, text = "Exit", command = window.destroy)
	exitButton.grid(row = 0, column = 1)
	#angle settings
	MODES = ["radians", "degrees", "gradians"]
	angleVar = StringVar(frame)
	angleVar.set(MODES[0])
	angleLabel = Label(frame, text="Mode",width=6)
	angleLabel.grid(row = 1, column = 0)
	angle = apply(OptionMenu, (frame, angleVar) + tuple(MODES))
	angle.grid(row = 1, column = 1)

	window.mainloop()

def generateGraph(settingsFrame, op, var, root, entry, minRange, maxRange, interval):
	boldFont = tkFont.Font(weight = "bold")
	if checkRanges(minRange, maxRange):
		DocumentDictionary.setUpperBound(maxRange)
		DocumentDictionary.setLowerBound(minRange)
		DocumentDictionary.setScale(interval)
		DocumentDictionary.setType(entry)
		#graphing.graph(root)
		op.append(entry)
		history = apply(OptionMenu, (root, var) + tuple(op))
		history.grid(row = 0, column = 7)

		history = apply(OptionMenu, (settingsFrame, var) + tuple(op))
		history.configure(highlightbackground = "#000000")
		history.grid(row = 0, column = 0)

		errorVar.set("")
	return

def checkRanges(minRange, maxRange):
	if minRange > maxRange:
		showError()
		return False
	else:
		return True

def showError(string):
	errorVar.set("ERROR: " + string)

def replaceEntry(entry, value):
	entry.delete(0,END)
	entry.insert(0, value)

def AddToEntry(entry, value):
	entry.insert(entry.index(INSERT), value)

#add value to entry box and put cursor in brackets
def AddToEntryBrackets(entry, value):
	entry.insert(entry.index(INSERT), value)
	entry.icursor(entry.index(INSERT)-1)

def UI():
	root = Tk()
	BUTTON_WIDTH = 5

	OPTIONS = ["x"]

	variable = StringVar(root)
	variable.set(OPTIONS[0])

	boldFont = tkFont.Font(weight = "bold")
	global errorVar
	errorVar = StringVar()

	#lambda: parseString(entry.get())


	#Setting up frames and root

	root.title('Name')
	root.configure(background = "#f2f2f2")
	frame = Frame(root, bg = "#f2f2f2")
	entryFrame = Frame(root, bg = "#f2f2f2")
	settingsFrame = Frame(root, bg = "#f2f2f2")
	space = Frame(frame, width = 20, height = 4, bg = "#f2f2f2")
	entry = Entry(entryFrame, width = 40)

	minLabel = Label(entryFrame, text = "Min")
	minLabel = Label(entryFrame, text = "Min", font = boldFont)
	minRange = Entry(entryFrame)
	minRange.insert(0, "-10")
	maxLabel = Label(entryFrame, text = "Max", font = boldFont)
	maxRange = Entry(entryFrame)
	maxRange.insert(0, "10")
	intervalLabel = Label(entryFrame, text = "Interval", font = boldFont)
	interval = Spinbox(entryFrame, increment = 0.1, from_ = 0.1, to = 10)

	historyButton = Button(root, text="History", width = BUTTON_WIDTH, command = lambda: replaceEntry(entry, variable.get()))
	historyButton.grid(row = 0, column = 8)

	errorLabel = Label(entryFrame, textvariable = errorVar, font = boldFont)

	goButton = Button(entryFrame, text = "Go", bg = "#333333", fg ="#ffffff", font = boldFont, command = lambda: generateGraph(settingsFrame, OPTIONS, variable, root, entry.get(), minRange.get(), maxRange.get(), interval.get()))

	#minimum ranch
	minLabel = Label(entryFrame, text = "Min", font = boldFont, bg = "#f2f2f2")
	minRange = Entry(entryFrame)
	minRange.insert(0, "-10")

	#maximum ranch
	maxLabel = Label(entryFrame, text = "Max", font = boldFont, bg = "#f2f2f2")
	maxRange = Entry(entryFrame)
	maxRange.insert(0, "10")

	#interval / scale
	intervalLabel = Label(entryFrame, text = "Interval", font = boldFont, bg = "#f2f2f2")
	interval = Spinbox(entryFrame, increment = 0.1, from_ = 0.1, to = 10)

	#history button
	historyButton = Button(settingsFrame, text="History", width = BUTTON_WIDTH, command = lambda: replaceEntry(entry, variable.get()),bg = "#d6d6c2", font = boldFont)
	historyButton.grid(row = 0, column = 1)
	historyButton.configure(highlightbackground = "#000000")

	#settings Button
	settingsButton = Button(settingsFrame, text="Settings", width = BUTTON_WIDTH, command = lambda: configureSettings(),bg = "#d6d6c2", font = boldFont)
	settingsButton.configure(highlightbackground = "#000000")
	settingsButton.grid(row = 0, column = 2)
	exitButton = Button(settingsFrame, text = "Exit Program", command = root.destroy,bg = "#d6d6c2", font = boldFont)
	exitButton.configure(highlightbackground = "#000000")
	exitButton.grid(row = 0, column = 3)
	#error
	errorLabel = Label(settingsFrame, textvariable = errorVar, font = boldFont, bg = "#f2f2f2")


	goButton = Button(entryFrame, text = "Go", bg = "#333333", fg ="#ffffff", font = boldFont, command = lambda: generateGraph(OPTIONS, variable, root, entry.get(), minRange.get(), maxRange.get(), interval.get()))
	entryFrame.grid(row = 0, column = 0)
	settingsFrame.grid(row = 1, column = 0)
	entry.grid(row = 0 , column = 1, padx = 0)
	goButton.grid(row = 0, column = 0, padx = 0)
	intervalLabel.grid(row = 0, column = 2)
	interval.grid(row = 0, column = 3, padx = 0)
	minLabel.grid(row = 0, column = 4)
	minRange.grid(row = 0, column = 5)
	maxLabel.grid(row = 0, column = 6)

	maxRange.grid(row = 0, column = 7)
	errorLabel.grid(row = 1, column = 3)

	maxRange.grid(row = 0, column = 7, padx = 0)

	errorLabel.grid(row = 0, column = 4)

	entry.focus_set()

	num = [None]*10
	operator = [None]*29

#Create all number buttons with their values
	num[0] = Button(frame, text=0, width = 13, command = lambda: AddToEntry(entry,0),bg = "#d6d6c2", font = boldFont)
	num[1] = Button(frame, text=1, width = BUTTON_WIDTH, command =lambda: AddToEntry(entry,1), bg = "#d6d6c2", font = boldFont)
	num[2] = Button(frame, text=2, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,2), bg = "#d6d6c2", font = boldFont)
	num[3] = Button(frame, text=3, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,3), bg = "#d6d6c2", font = boldFont)
	num[4] = Button(frame, text=4, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,4), bg = "#d6d6c2", font = boldFont)
	num[5] = Button(frame, text=5, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,5), bg = "#d6d6c2", font = boldFont)
	num[6] = Button(frame, text=6, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,6), bg = "#d6d6c2", font = boldFont)
	num[7] = Button(frame, text=7, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,7), bg = "#d6d6c2", font = boldFont)
	num[8] = Button(frame, text=8, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,8), bg = "#d6d6c2", font = boldFont)
	num[9] = Button(frame, text=9, width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,9), bg = "#d6d6c2", font = boldFont)
	num[0].configure(highlightbackground = "#000000")
#create all operator buttons with thier values
	operator[0] = Button(frame, text='.', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"."),bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[1] = Button(frame, text='+', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"+"),bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[2] = Button(frame, text='-', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"-"),bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[3] = Button(frame, text='*', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"*"),bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[4] = Button(frame, text='/', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"/"),bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[5] = Button(frame, text='sin(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"sin()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[6] = Button(frame, text='cos(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"cos()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[7] = Button(frame, text='tan(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"tan()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[8] = Button(frame, text='sinh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"sinh()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[9] = Button(frame, text='cosh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"cosh()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[10] = Button(frame, text='tanh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"tanh()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[11] = Button(frame, text='arcsin(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arcsin()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[12] = Button(frame, text='arccos(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arccos()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[13] = Button(frame, text='arctan(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arctan()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[14] = Button(frame, text='arcsinh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arcsinh()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[15] = Button(frame, text='arccosh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arccosh()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[16] = Button(frame, text='arctanh(x)', width = 10, command = lambda: AddToEntryBrackets(entry,"arctanh()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[17] = Button(frame, text='sqrt(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"sqrt()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[18] = Button(frame, text='^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"^()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[19] = Button(frame, text='1/x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"1/()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[20] = Button(frame, text='10^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"10^()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[21] = Button(frame, text='e^x', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,", bg = ""e^()"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[22] = Button(frame, text='pi', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"3.14"), bg = "#333333", fg ="#ffffff", font = boldFont)
	operator[23] = Button(frame, text='!', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"!"), bg = "#333333", fg = "#ffffff", font = boldFont)
	operator[24] = Button(frame, text='log(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"log()"),bg = "#333333", fg = "#ffffff", font = boldFont)
	operator[25] = Button(frame, text='ln(x)', width = BUTTON_WIDTH, command = lambda: AddToEntryBrackets(entry,"ln()"),bg = "#333333", fg = "#ffffff", font = boldFont)
	operator[26] = Button(frame, text='(', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"("),bg = "#333333", fg = "#ffffff", font = boldFont)
	operator[27] = Button(frame, text=')', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,")"),bg = "#333333", fg = "#ffffff", font = boldFont)
	operator[28] = Button(frame, text='x', width = BUTTON_WIDTH, command = lambda: AddToEntry(entry,"x"),bg = "#333333", fg = "#ffffff", font = boldFont)
	#COLOUR STUFF
	for i, val in enumerate(operator):
		operator[i].configure(highlightbackground = "#000000")
	#COLOUR STUFF
	for i, val in enumerate(num):
		num[i].configure(highlightbackground = "#000000")


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
	operator[1].grid(row = 0,column = 3)
	operator[2].grid(row = 1,column = 3)
	operator[3].grid(row = 2,column = 3)
	operator[4].grid(row = 3,column = 3)
	operator[5].grid(row = 0,column = 5)
	operator[6].grid(row = 1,column = 5)
	operator[7].grid(row = 2,column = 5)
	operator[8].grid(row = 3,column = 5)
	operator[9].grid(row = 0,column = 6)
	operator[10].grid(row = 1,column = 6)
	operator[11].grid(row = 2,column = 6)
	operator[12].grid(row = 3,column = 6)
	operator[13].grid(row = 0,column = 7)
	operator[14].grid(row = 1,column = 7)
	operator[15].grid(row = 2,column = 7)
	operator[16].grid(row = 3,column = 7)
	operator[17].grid(row = 0,column = 8)
	operator[18].grid(row = 1,column = 8)
	operator[19].grid(row = 2,column = 8)
	operator[20].grid(row = 3,column = 8)
	operator[21].grid(row = 0,column = 9)
	operator[22].grid(row = 1,column = 9)
	operator[23].grid(row = 2,column = 9)
	operator[24].grid(row = 3,column = 9)
	operator[25].grid(row = 0,column = 10)
	operator[26].grid(row = 1,column = 10)
	operator[27].grid(row = 2,column = 10)
	operator[28].grid(row = 3,column = 10)
	root.wm_title("Ranch Calc 3.0")

	root.mainloop()
