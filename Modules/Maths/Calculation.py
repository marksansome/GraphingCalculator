#File for managing calculations
from Global import Tree

#We need to convert like strings into functions calls for sin etc
#Boring but looks easy

def process(nodeIndex):
	left = Tree.getAtIndex(Tree.leftChildIndex(nodeIndex))
	right = Tree.getAtIndex(Tree.rightChildIndex(nodeIndex))
	parent = Tree.getAtIndex(nodeIndex)
	calculate(parent, left, right)

def calculate(parent, left, right):
	return 1

