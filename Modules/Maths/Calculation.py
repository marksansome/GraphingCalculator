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
		print ("Value Error")

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

def div(left, right):
	#TODO: division by zero
	try:
		result = left/right
		return result
	except ZeroDivisionError:
		return None

def sinus(left, right):
	return math.sin(left)

def cosinus(left, right):
	return math.cos(left)

def tangente(left, right):
	#TODO: domain range
	return math.tan(left)

def arcsinus(left, right):
	return math.sin(left)

def arccosinus(left, right):
	return math.acos(left)

def arctangente(left, right):
	return math.atan(left)

def sinhyp(left, right):
	return math.sinh(left)

def coshyp(left, right):
	return math.cosh(left)

def tanhyp(left, right):
	return math.tanh(left)

def arcsinhyp(left, right):
	return math.asinh(left)

def arccoshyp(left, right):
	return math.acosh(left)

def arctanhyp(left, right):
	return math.atanh(left)

def squareroot(left, right):
	return math.sqrt(left)

def power(left, right):
	return math.pow(left, right)

def log(left, right):
	return math.log10(left)

def ln(left, right):
	return math.log(left)

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
	"/" : div,
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
