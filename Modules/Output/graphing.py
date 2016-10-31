#!/usr/bin/python
import Tkinter
import tkMessageBox

#printing points
def drawPoints(x, y, height, width, canvas):
	scale = width / (x[-1] + x[-1])
	for i in range(len(x)):
		x[i] = (x[i] * scale + width/2)
		y[i] = (-y[i] * scale + height/2)
		canvas.create_oval(x[i], y[i], x[i], y[i])

	for i in range(len(x) - 1):
		canvas.create_line(x[i], y[i], x[i+1], y[i+1])

def graph(root, x, y):
	height = 500
	width = 400

	# draws canvas and lines
	canvas = Tkinter.Canvas(root, bg="white", height=height, width=width)
	horLine = canvas.create_line(width/2, 0, width/2, height, fill="black")
	vertLine= canvas.create_line(0, height/2, width, height/2, fill="black")

	#button to quit
	quitButton = Tkinter.Button(root, text ="Close Graphing Calculator", command = root.destroy)

	drawPoints(x, y, height, width, canvas)
	canvas.grid(row = 4, column = 0)
	quitButton.grid()
