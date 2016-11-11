#!/usr/bin/python
import Tkinter
import tkMessageBox
import numbers
from Modules.DataStructures import DocumentDictionary

#printing points
def drawPoints(x, y, height, width, canvas):
<<<<<<< HEAD
	scaleY = height / 20
	scaleX = width / (float(DocumentDictionary.getUpperBound(DocumentDictionary.dictionary)) - (float(DocumentDictionary.getLowerBound(DocumentDictionary.dictionary))))
	
=======
	scaleY = height / (max(y) - min(y))
	scaleX = width / (float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound())))
>>>>>>> c6b131c9d0d977f16cc60953f9cd5461167abdc4
	for i in range(len(x)):
		x[i] = (x[i] * scaleX + width/2)
		y[i] = (-y[i] * scaleY + height/2)
		canvas.create_oval(x[i], y[i], x[i], y[i])

	for i in range(len(x) - 1):
		canvas.create_line(x[i], y[i], x[i+1], y[i+1])

def drawLines(x, height, width, canvas):
	scaleX = width / (float(DocumentDictionary.getUpperBound(DocumentDictionary.dictionary)) - (float(DocumentDictionary.getLowerBound(DocumentDictionary.dictionary))))

	horLine= canvas.create_line(0, height/2, width, height/2, fill="black")
	for i in range(len(x)):
		if x[i] == 0.0:
			vertLine = canvas.create_line(x[i] * scaleX + width/2, 0, x[i] * scaleX + width/2, height, fill="black")
		elif x[i] < 0.0 and x[i+1] > 0.0:
			vertLine = canvas.create_line(((x[i] - x[i+1]) / 2) * scaleX + width/2, 0, ((x[i] - x[i+1]) / 2) * scaleX + width/2, height, fill="black")

def graph(root):
	height = 500
	width = 400
<<<<<<< HEAD
	x = DocumentDictionary.getTableOfValues(DocumentDictionary.dictionary)['xValues']
	y = DocumentDictionary.getTableOfValues(DocumentDictionary.dictionary)['yValues']
	
=======

>>>>>>> c6b131c9d0d977f16cc60953f9cd5461167abdc4
	# draws canvas and lines
	canvas = Tkinter.Canvas(root, bg="white", height=height, width=width)
	drawLines(x, height, width, canvas)
	
	#button to quit
	quitButton = Tkinter.Button(root, text ="Close Graphing Calculator", command = root.destroy)
<<<<<<< HEAD

=======
	x = DocumentDictionary.getTableOfValues()['xValues']
	y = DocumentDictionary.getTableOfValues()['yValues']
>>>>>>> c6b131c9d0d977f16cc60953f9cd5461167abdc4
	drawPoints(x, y, height, width, canvas)

	canvas.grid(row = 4, column = 0)
	quitButton.grid()
