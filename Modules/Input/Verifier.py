#!/usr/bin/python
#from Modules.DataStructures import MathFunctions

#
#   verify
#   Parse and validate into parenthesized string.
#   IN: (String) The expression.
#   OUT: (String) The validated expression.
#
def verify(string):
    bracketOpen = 0
    pStr = ""

    string = string.replace(" ","")

    length = len(string)
    i = 0
    specOp = False

    while i < length:
        fop = False

        #if string[i] == '(':
        #    bracket = True

        #   Open always on empty brackets
        if bracketOpen == 0:
            pStr += str("(")
            bracketOpen += 1

        #   If number or function open a new bracket
        for op in ('*','/','+','^','-'):
            if string[i] == op:
                fop = True
        if not fop and not specOp:
            pStr += str("(")
            bracketOpen += 1

        fop = False

        if i + 1 != length:
            #   If *,/,^, or variable write number and operand
            for op in ('*','/','^','x'):
                if string[i+1] == op:
                    fop = True
                    pStr += str(string[i])
                    if not specOp:
                        specOp = True
                    else:
                        pStr += str(")")
                        bracketOpen -= 1
                    pStr += str(string[i+1])
            #   Else close bracket and write operator
            if not fop:
                specOp = False
                pStr += str(string[i] + ")" + string[i+1])
                bracketOpen-=1
        else:
            pStr += str(string[i])
        i += 2
    #   When we hit the end of the string we need to close all of the brackets left open
    while bracketOpen != 0:
        pStr += str(")")
        bracketOpen -= 1
    return pStr

#eq = "3^(3^2)"
eq = "2*3+2"
#eq = "2*3*2"
print verify(eq)
