#!/usr/bin/python
import Tkinter
import tkMessageBox
import numbers
from Modules.DataStructures import DocumentDictionary

#printing points
def drawPoints(x, y, height, width, canvas):
	scaleY = height / 20
	scaleX = width / ((float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound()))) / float(DocumentDictionary.getScale())) * 10
	X = []
	Y = []
	for i in range(len(x)):
		print x[i], ",", y[i]
		X.append(x[i] * scaleX + width/2)
		Y.append(-y[i] * scaleY + height/2)
		print X[i] , "," , Y[i]
		canvas.create_oval(X[i], Y[i], X[i], Y[i])
		drawLines(X, height, width, canvas)

	for i in range(len(x) - 1):
		canvas.create_line(X[i], Y[i], X[i+1], Y[i+1])

def drawLines(x, height, width, canvas):
	scaleX = width / (float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound())))

	horLine= canvas.create_line(0, height/2, width, height/2, fill="black")
	for i in range(len(x)):
		if x[i] == 0.0:
			vertLine = canvas.create_line(x[i] * scaleX + width/2, 0, x[i] * scaleX + width/2, height, fill="black")
		elif x[i] < 0.0 and x[i+1] > 0.0:
			vertLine = canvas.create_line(((x[i] - x[i+1]) / 2) * scaleX + width/2, 0, ((x[i] - x[i+1]) / 2) * scaleX + width/2, height, fill="black")

def graph(root):
	height = 500
	width = 400

	x = DocumentDictionary.getTableOfValues()['xValues']
	y = DocumentDictionary.getTableOfValues()['yValues']

	# draws canvas and lines
	canvas = Tkinter.Canvas(root, bg="white", height=height, width=width)

	x = DocumentDictionary.getTableOfValues()['xValues']
	y = DocumentDictionary.getTableOfValues()['yValues']
	drawPoints(x, y, height, width, canvas)

	canvas.grid(row = 4, column = 0)
