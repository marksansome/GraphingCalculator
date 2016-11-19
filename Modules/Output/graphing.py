#!/usr/bin/python
import Tkinter
import tkMessageBox
from Modules.DataStructures import DocumentDictionary

colours = ["black", "red", "green", "blue", "cyan", "yellow","magenta"]
currentColour = 0

#printing points
def drawPoints(x, y, height, width, canvas):
	scaleX = width / ((float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound()))) / float(DocumentDictionary.getScale())) * 10
	#scaleY = height / ((max(y) - min(y)) / float(DocumentDictionary.getScale())) * 10
	X = []
	Y = []
	for i in range(len(x)):
		if isinstance(y[i], (int, float)):
			X.append(x[i] * scaleX + width/2)
			Y.append(-y[i] * scaleX + height/2)
			#draws points, uncomment to enable
			#canvas.create_oval(X[i], Y[i], X[i], Y[i])

	global currentColour
	for i in range(len(X) - 1):
		canvas.create_line(X[i], Y[i], X[i+1], Y[i+1], fill=colours[currentColour], width=2)
	if currentColour == 6:
		currentColour = 0;
	else:
		currentColour = currentColour + 1

def drawLines(height, width, canvas):
	scale = width / ((float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound()))) / float(DocumentDictionary.getScale())) * 10
	horLine= canvas.create_line(0, height/2, width, height/2, fill="black")
	vertLine = canvas.create_line(width/2, 0, width/2, height, fill="black")

	for x in range(0, width, int(scale)):
		canvas.create_line(x,height/2 + 4,x,height/2 -4, fill="black")

	canvas.create_text(10 ,height / 2 + 10, text= DocumentDictionary.getLowerBound(), tag = "cunt")
	canvas.create_text(width - 10 ,height / 2 + 10, text= DocumentDictionary.getUpperBound(), tag = "cunt")

	for y in range(0, height, int(scale)):
		canvas.create_line(width/2 + 4, y, width/2 -4,y, fill="black")
	canvas.create_text(width/2 + 10, 10, text= DocumentDictionary.getUpperBound(), tag = "cunt")
	canvas.create_text(width/2 + 10, height - 10, text= DocumentDictionary.getLowerBound(), tag = "cunt")


def graph(canvas, height, width):
	canvas.delete("cunt")
	x = DocumentDictionary.getTableOfValues()['xValues']
	y = DocumentDictionary.getTableOfValues()['yValues']
	drawLines(height, width, canvas)
	drawPoints(x, y, height, width, canvas)
