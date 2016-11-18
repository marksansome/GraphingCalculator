#!/usr/bin/python

from Modules.Input.Verifier import parseStringToList
from Modules.DataStructures.MathFunctions import *
from Modules.Output.UI import showError

#
#   validate
#   Takes a string and checks if it has any invalid mathematical syntax.
#   IN: (String) The expression validate.
#
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
        elif not item.isdigit() and item != 'x' and not isOperator(item) and not isConstant(item):
            if item not in MathFunctions:
                error = "Invalid function in equation"
        elif isOperator(item):
            nextI = eqList[i+1]
            if isOperator(nextI):
                error = "Two consecutive operators"
    if parentheses != 0:
        error = "Parentheses mismatch"
    if error:
        showError(error)
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
