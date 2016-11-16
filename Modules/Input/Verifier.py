#!/usr/bin/python

BEDMAS = {
    4 : ['!'],
    3 : ['^'],
    2 : ['*','/'],
    1 : ['+','-'],
}

parse = []


#
#   TODO: Brackets and functions and factorials....
#   BUG:  Fix the last index issue... Where brackets get carried into the last term
#

#
#   parseStringToList
#   Takes a string and groups each term in the expression into a list.
#   IN: (String) The expression.
#   OUT: (List) The parsed expression.
#
def parseStringToList(string):
    length = len(string)

    parseString = ""
    index = 0
    found = False
    sIndex = 0
    #   Begin iterating the string
    while index < length:
        #print parse
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
                if parseString is not "":
                    parse.append(parseString)
                parseString = ""
                if parse[-1] not in ['*','/','+','-','^']:
                    #   If the previous item parsed is a number then lets add a multiplication sign
                    parse.append("*")
                    parse.append(string[index])
                else:
                    #   Otherwise treat as x without coefficient
                    parse.append(string[index])
            #    If current index is not an operator then we should concat to a string
            elif string[index] not in ['*','/','+','-','^','(',')']:
                parseString += string[index]
            #   Otherwise the value is an operator and we should the previous term, then the operator
            else:
                if parseString is not "":
                    parse.append(parseString)
                parseString = ""
                parse.append(string[index])
        index += 1

    return parse


def setNestedBrackets(parse):
    parseLength = len(parse)
    openBracket = 0
    sIndex = 0
    k = 0
    while k < parseLength:
        if parse[k] == '(':
            openBracket += 1
            if sIndex == 0:
                sIndex = k + 1
        elif parse[k] == ')':
            openBracket -= 1
            if openBracket == 0:
                #   We're at the end of this bracket set
                myStr = verify(parse[sIndex:k])
                print myStr + " + " + str(parse)
                print "sIndex : " +str(sIndex) + " k " + str(k)
                print "rm: ",
                for i in range(sIndex-1, k-sIndex+2):
                    print parse.pop(sIndex-1),
                #   Combine them into one element
                print "Insert " + str(myStr)
                parse.insert(sIndex-1,myStr)
                return parse
        k += 1

#
#   verify
#   Parse and validate into parenthesized string.
#   IN: (String) the equation to parse.
#   OUT: (String) The validated expression.
#
def verify(parse):

    parseLength = len(parse)
    #print parse
    openBracket = 0
    sIndex = 0

    #   For each BEDMAS operation
    for i in range(4,0,-1):
        k = 0
        setNestedBrackets(parse)
        #print parse
        #   For each element of the parse'd list
        while k < parseLength:
            #   Check for brackets
            if i == 5:
                #   Count the number of nested brackets
                continue

            elif i is not 5:
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
            #   Recalculate the length of the list and increment the counter
            parseLength = len(parse)
            k+=1
    return parse.pop(0)

#eq = "(1^(3+2))^2+(4+9)"
#eq = "17-2*3+7"
#eq = "(2+(3/9))*2+(2+4)+8"
#eq = "(2+(3/9))*2"
#eq = "(1+2)^3*4"
#eq = "5+6*7-9/1"
#eq = "1.2    +x*2/9+8+sin(8+2)"
eq = "sin(8+2)"
print "original: " + eq
parse = parseStringToList(eq)
print verify(parse)
#print parseStringToList(eq)
