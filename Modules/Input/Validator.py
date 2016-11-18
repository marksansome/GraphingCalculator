#!/usr/bin/python

from Modules.Input.Verifier import parseStringToList
from Modules.DataStructures.MathFunctions import *

def validate(equation):
    eqList = parseStringToList(equation)
    error = None
    print eqList
    parentheses = 0
    for i,item in enumerate(eqList):
        if item is '(':
            parentheses += 1
            nextI = eqList[i+1]
        elif item is ')':
            parentheses += -1
        elif not item.isdigit() and item != 'x' and not isConstant(item):
            if item not in MathFunctions:
                error = "Invalid function in equation"
        elif isOperator(item):
            nextI = eqList[i+1]
            if isOperator(nextI):
                error = "Two consecutive operators"
    if parentheses != 0:
        error = "Parentheses mismatch"
    if error:
        print error
    else:
        print "okay"

def isOperator(c):
	if(c == '+' or c == '-' or c == '*' or c =='/' or c == '^'):
		return 1
	return 0

def isConstant(c):
    if c == 'pi' or c == 'e':
        return 1
    return 0
