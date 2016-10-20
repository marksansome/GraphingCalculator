#File responsible for managing calculations at the finest (i.e bottom of the tree)
from Global import Tree

#process one node that is parent of operands nodes
def process(nodeIndex):
	#TODO:be careful about types, we need to make sure we're working with integers, but this need to be handled beforehand
	left = float(Tree.getAtIndex(Tree.leftChildIndex(nodeIndex)))
	right = float(Tree.getAtIndex(Tree.rightChildIndex(nodeIndex)))
	parent = Tree.getAtIndex(nodeIndex)

	result = calculate(parent, left, right)
	Tree.setAtIndex(nodeIndex, result)
	Tree.removeChilds(nodeIndex)

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

# map the inputs to the function blocks
operators = {"+" : addition,
			 "*" : multiplication,
			 "-" : substraction,
			 "/" : division
}