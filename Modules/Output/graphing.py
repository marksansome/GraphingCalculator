#!/usr/bin/python
import Tkinter
import tkMessageBox
from Modules.DataStructures import DocumentDictionary

#printing points
def drawPoints(x, y, height, width, canvas):
	scale = width / ((float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound()))) / float(DocumentDictionary.getScale())) * 10
	X = []
	Y = []
	for i in range(len(x)):
		X.append(x[i] * scale + width/2)
		Y.append(-y[i] * scale + height/2)
		#draws points, uncomment to enable
		#canvas.create_oval(X[i], Y[i], X[i], Y[i])

	for i in range(len(x) - 1):
		canvas.create_line(X[i], Y[i], X[i+1], Y[i+1])

def drawLines(height, width, canvas):
	scale = width / ((float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound()))) / float(DocumentDictionary.getScale()))

	horLine= canvas.create_line(0, height/2, width, height/2, fill="black")
	vertLine = canvas.create_line(width/2, 0, width/2, height, fill="black")

def graph(canvas):
	height = 400
	width = 400

	x = DocumentDictionary.getTableOfValues()['xValues']
	y = DocumentDictionary.getTableOfValues()['yValues']
	drawPoints(x, y, height, width, canvas)
