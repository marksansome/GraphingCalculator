#!/usr/bin/python
import Tkinter
import tkMessageBox

#printing points
def drawPoints(x, y, scale):
	for i in range(len(x)):
		x[i] = (x[i] * scale + width/2)
		y[i] = (-y[i] * scale + height/2)
		canvas.create_oval(x[i], y[i], x[i], y[i])

	for i in range(len(x) - 1):
		canvas.create_line(x[i], y[i], x[i+1], y[i+1])

#def zoomIn():
#	scale = scale * 2
#	x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
#	y = [100,81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81,100]
#	drawPoints(x,y,scale)

x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y = [100,81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81,100]

root = Tkinter.Tk()
height = 500
width = 400
scale = 10

# draws canvas and lines
canvas = Tkinter.Canvas(root, bg="white", height=height, width=width)
horLine = canvas.create_line(width/2, 0, width/2, height, fill="black")
vertLine= canvas.create_line(0, height/2, width, height/2, fill="black")

#button to quit
quitButton = Tkinter.Button(root, text ="Close Graph", command = root.destroy)

#buttons to zoom
#zoomInButton = Tkinter.Button(root, text = "Zoom In", command = drawPoints(x,y,scale * 10))
#zoomOutButton = Tkinter.Button(root, text = "Zoom In", command = zoomOut())
#zoomInButton.pack()

drawPoints(x, y, scale)
canvas.pack()
quitButton.pack()
root.mainloop()
