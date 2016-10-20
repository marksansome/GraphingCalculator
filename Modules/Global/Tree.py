
table = [None, "+", 3, 4]

def createTable():
	table = []

def leftChildIndex(index):
	return 2*index

def rightChildIndex(index):
	return (2*index)+1

def parentIndex(index):
	if index%2 == 0:
		return index/2
	else:
		return (index-1)/2

def getAtIndex(index):
	return table[index]

def setAtIndex(index, value):
	table[index] = value

def removeChilds(index):
	setAtIndex(leftChildIndex(index), None)
	setAtIndex(rightChildIndex(index), None)