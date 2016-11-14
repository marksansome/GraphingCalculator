#!/usr/bin/python
#from Modules.DataStructures import MathFunctions
MathFunctions = {
    'sin' : "",
    'cos' : "",
    'tan' : "",
    'arcsin' : "",
    'arccos' : "",
    'arctan' : "",
    'sinh' : "",
    'cosh' : "",
    'tanh' : "",
    'arcsinh' : "",
    'arccosh' : "",
    'arctanh' : "",
    'sqrt' : "",
    'log' : "",
    'ln' : "",
}

myList = [None] * 20

def split(equation):
	parentheses = 0
	count = -1
	for i in equation:
		count += 1
		if i == '(':
			parentheses += 1
		elif i == ')':
			parentheses -= 1
		if(parentheses == 1 and isOperator(i)):
			return count
	return -1

def isOperator(c):
	if(c == '+' or c == '-' or c == '*' or c =='/' or c == '^'):
		return 1
	return 0

def parseString(equation, index):
	length = len(equation)
	for function in MathFunctions:
		size = len(function)
		if function in equation[1:size+1]:
			myList[index] = function
			parseString(equation[size+1:length], index*2)
			return

	position = split(equation)
	if(position != -1):
		parent = equation[position]
		myList[index] = parent
	else:
		myList[index] = equation.strip('()')
	if(position != -1):
		print equation
		parseString(equation[1:position], index * 2)
		parseString(equation[position+1:length-1], index * 2 + 1)
	return

#equation = "(sin(cos(0)))"
#equation = "((5+6)*(9+8))"
#equation = "((2+2)*(sin(4.0+5.0)))"
equation = "(log(5+5))"
#equation = "(arcsinh(cos(pi)))"
parseString(equation,1)
print myList
