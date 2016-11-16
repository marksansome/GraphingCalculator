#File responsible for managing calculations at the finest (i.e bottom of the tree)
from __future__ import division
from Modules.DataStructures import Tree
import math

#process one node that is parent of operands nodes
def process(tree, nodeIndex):
	#security layer
	try:
		if tree[Tree.leftChildIndex(nodeIndex)] != None:
			left = float(tree[Tree.leftChildIndex(nodeIndex)])
		else:
			left = None
		if tree[Tree.rightChildIndex(nodeIndex)] != None:
			right = float(tree[Tree.rightChildIndex(nodeIndex)])
		else:
			right = None

		parent = tree[nodeIndex]
		#TODO:this is where i want to add the domain out of bound error
		result = calculate(parent, left, right)
		tree[nodeIndex] = result
		Tree.removeChilds(tree, nodeIndex)
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
		return math.sin(left)
	elif left == None:
		return math.sin(right)

def cosinus(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.cos(left)
	elif left == None:
		return math.cos(right)

def tangente(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	#TODO: domain range
	if right == None:
		return math.tan(left)
	elif left == None:
		return math.tan(right)

def arcsinus(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.sin(left)
	elif left == None:
		return math.sin(right)

def arccosinus(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.acos(left)
	elif left == None:
		return math.acos(right)

def arctangente(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.atan(left)
	elif left == None:
		return math.atan(right)

def sinhyp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.sinh(left)
	elif left == None:
		return math.sinh(right)

def coshyp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.cosh(left)
	elif left == None:
		return math.cosh(right)

def tanhyp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.tanh(left)
	elif left == None:
		return math.tanh(right)

def arcsinhyp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.asinh(left)
	elif left == None:
		return math.asinh(right)

def arccoshyp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.acosh(left)
	elif left == None:
		return math.acosh(right)

def arctanhyp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.atanh(left)
	elif left == None:
		return math.atanh(right)

def squareroot(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.sqrt(left)
	elif left == None:
		return math.sqrt(right)

def power(left, right):
	#TODO:confirm this
	return math.pow(left, right)

def log(left, right):
	#TODO:confirm this too
	return math.log(right, left)

def ln(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		#TODO: base e right?
		return math.log(left, math.e)
	elif left == None:
		return math.log(right, math.e)

def exp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.exp(left)
	elif left == None:
		return math.exp(right)


# map the inputs to the function blocks
operators = {
	"+" : addition,
	"*" : multiplication,
	"-" : substraction,
	"/" : division,
	"sin": sinus,
	"cos": cosinus,
	"tan:": tangente,
	"arcsin": arcsinus,
	"arccos": arccosinus,
	"arctan": arctangente,
	"sinh": sinhyp,
	"cosh": coshyp,
	"tanh": tanhyp,
	"arcsinh": arcsinhyp,
	"arccosh": arccoshyp,
	"arctanh": arctanhyp,
	"sqrt": squareroot,
	"^": power,
	"log": log,
	"ln": ln,
	"e^": exp,
}
