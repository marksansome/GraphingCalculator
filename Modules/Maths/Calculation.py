#File responsible for managing calculations at the finest (i.e bottom of the tree)
from Global import Tree
import math

#process one node that is parent of operands nodes
def process(nodeIndex):
	#security layer
	try:
		#TODO:be careful about types, we need to make sure we're working with integers, but this need to be handled beforehand
		if Tree.getAtIndex(Tree.leftChildIndex(nodeIndex)) != None:
			left = float(Tree.getAtIndex(Tree.leftChildIndex(nodeIndex)))
		else:
			left = None
		if Tree.getAtIndex(Tree.rightChildIndex(nodeIndex)) != None:
			right = float(Tree.getAtIndex(Tree.rightChildIndex(nodeIndex)))
		else:
			right = None

		parent = Tree.getAtIndex(nodeIndex)

		result = calculate(parent, left, right)
		Tree.setAtIndex(nodeIndex, result)
		Tree.removeChilds(nodeIndex)
	except ValueError:
		print "Value Error"
#calculate parent value given two operands child nodes
def calculate(parent, left, right):
	result = operators[parent](left, right)
	return result


# define the different function blocks
def addition(left, right):
	return left + right

def multiplication(left, right):
	return left * right

def substraction(left, right):
	return left - right

def division(left, right):
	#TODO:manage types to get floats as a result
	return left / right

def sinus(left, right):
	#Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.sin(float(left))
	elif left == None:
		return math.sin(right)

# map the inputs to the function blocks
operators = {"+" : addition,
			 "*" : multiplication,
			 "-" : substraction,
			 "/" : division,
			 "sin": sinus,

}