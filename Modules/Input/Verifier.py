#!/usr/bin/python

from Modules.DataStructures.MathFunctions import *
from Modules.Maths.FillTree import *
from Modules.Maths.TreeProcessing import *

eqList = [None] * 100

#
#   validate
#   Takes a string and checks if it has any invalid mathematical syntax.
#   IN: (String) The expression validate.
#

def runValidate(eq):
    global eqList
    eqList = [None] * 100
    return validate(eq)

def validate(equation):
    eqList = parseStringToList(equation)
    print eqList
    error = 0
    parentheses = 0
    for i,item in enumerate(eqList):
        if item is '(':
            parentheses += 1
            nextI = eqList[i+1]
        elif item is ')':
            parentheses += -1
        elif not item.isdigit() and item != 'x' and not isOperator(item) and not isConstant(item):
            if item not in MathFunctions:
                error = 1
        elif isOperator(item):
            nextI = eqList[i+1]
            if isOperator(nextI):
                error = 2
    if parentheses != 0:
        error = 3
    return error

def isOperator(c):
	if(c == '+' or c == '-' or c == '*' or c =='/' or c == '^'):
		return 1
	return 0

def isConstant(c):
    if c == 'pi' or c == 'e':
        return 1
    return 0

def getErrorMsg(errorInt):
   if errorInt == 1:
       return "Invalid function in equation"
   if errorInt == 2:
       return "Two consecutive operators"
   if errorInt == 3:
       return "Parentheses mismatch"

#
#   Create a table indexing higher order of BEDMAS + Factorials
#
BEDMAS = {
    4 : ['!'],
    3 : ['^'],
    2 : ['*','/'],
    1 : ['+','-'],
}

#
#   Table containing function names TODO: Remove for centralized table????
#
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

parse = []

#
#   parseStringToList
#   Takes a string and groups each term in the expression into a list.
#   IN: (String) The expression to split.
#   OUT: (List) The parsed expression.
#
def parseStringToList(string):
    length = len(string)

    parseString = ""
    index = 0
    sIndex = 0
    #   Begin iterating the string
    while index < length:
        #   Ensure we are not looking at a space
        if string[index] is not ' ':
            #   If it's the last item make sure we add it
            if index+1 == length:
                if string[index] == ')':
                    parse.append(parseString)
                    parse.append(string[index])
                else:
                    parseString += string[index]
                    parse.append(parseString)
            #   If the term is an x decide how to treat it
            elif string[index] is 'x':
                #   If there was a term before x we need to multipy and bracket it to preserve order
                if parseString is not "":
                    parse.append(parseString)
                    parse.append("*")
                    parse.append("x")
                    parseString = ""
                #   Otherwise we just want to append an x
                else:
                    parse.append("x")
            #    If current index is not an operator then we should concat to a string
            elif string[index] not in ['*','/','+','-','^','(',')']:
                parseString += string[index]
            #   Otherwise the value is an operator and we should the previous term, then the operator
            else:
                #   If there are terms to print print em
                if parseString is not "":
                    parse.append(parseString)
                #   Clean up parse string
                parseString = ""
                parse.append(string[index])
        index += 1

    return parse

#
#   setNestedBrackets
#   Find all sets of brackets and verify them recursivly.
#   IN: (List) The list to search for bracket sets.
#   OUT: (List) The condensed list expression.
#
def setNestedBrackets(parse):
    parseLength = len(parse)
    openBracket = 0
    sIndex = -1
    k = 0
    #   For every element in the list
    while k < parseLength:
        #   When we hit an open bracket we need to mark the start and find the end
        if parse[k] == '(':
            openBracket += 1
            if sIndex == -1:
                #   Start index of brackets
                sIndex = k
        elif parse[k] == ')':
            openBracket -= 1
            #   If we're at the end of the bracket set (openBracket == 0) then we need to check for nested
            if openBracket == 0:
                #   Nested check
                if '(' in  parse[sIndex+1:k]:
                    someList = setNestedBrackets(parse[sIndex+1:k])
                #   Otherwise we're done and we need to parenthesize the list, call verify
                myStr = verify(parse[sIndex+1:k])
                #   Merc the items we've condensed
                for i in range(0, k-sIndex+1):
                    parse.pop(sIndex)
                #   Combine them into one element
                if len(myStr) is 1:
                    parse.insert(sIndex,"(" + myStr + ")")
                else:
                    parse.insert(sIndex,myStr)
                return parse
        k += 1

#
#   verify
#   Parse and validate into parenthesized string.
#   IN: (List) the pre parsed list. (See parseStringToList)
#   OUT: (String) The validated expression.
#
def verify(parse):
    parseLength = len(parse)
    openBracket = 0
    sIndex = 0
    counter = 0

    #   We need to count the brackets and run setNestedBrackets for each
    for a in parse:
        if a == '(':
            counter+=1
    for m in range(0,counter):
        setNestedBrackets(parse)
    #   For each BEDMAS operation
    for i in range(4,0,-1):
        k = 0
        #   For each element of the parse'd list
        while k < parseLength:
            #   Check to see if the current index of the list is an operator
            if parse[k] in BEDMAS[i]:
                #   Take left and right of the equation
                myStr = "(" + parse[k-1] + parse[k] + parse[k+1] + ")"
                #   Remove the three items from the list
                parse.pop(k-1)
                parse.pop(k-1)
                parse.pop(k-1)
                #   Combine them into one element
                parse.insert(k-1,myStr)
                #   Reset the parse index counter, and look again for same order operations
                k = 0
            elif parse[k] in MathFunctions.keys():
                myStr = "(" + parse[k] + parse[k+1] + ")"
                #   Remove the three items from the list
                parse.pop(k)
                parse.pop(k)
                #   Combine them into one element
                parse.insert(k,myStr)
                #   Reset the parse index counter, and look again for same order operations
                k = 0
            #   Recalculate the length of the list and increment the counter
            parseLength = len(parse)
            k+=1
    return parse.pop(0)


def goRunAll(string):
    number = runValidate(string)
    if number is 0:
        initList()
        someList = parseStringToList(string)
        parenthesizedString = verify(someList)
        goFill(parenthesizedString)
        go()
    else:
        print string + " ",
        print getErrorMsg(number)
    return number
