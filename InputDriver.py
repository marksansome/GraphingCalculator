#!/usr/bin/python

#
#   Verify Driver
#   Verify the functions within verifier
#
eq = "2x+5"
ans = "((2*x)+5)"
ansVerified = verify(eq)
assertEqual("Assert that the expression original expression " + eq + " is equal to " + ans + " [compared to " + ansVerified + "]",ansVerified,ans)


#
#
#

#eq = "(1^(3+2))^2+(4+9)"
#eq = "17-2*3+7"
#eq = "(2+(3/9))*2+(2+4)+8"
#eq = "(2+3)*4+(5/9)"
#eq = "(2+(3/9))*2"
#eq = "(1+2)^3*4"
#eq = "5+6*7-9/1"    #((5+(6*7))-(9/1))
#eq = "1.2    +x*2/9+8+tan(2x^2)" #(((1.2+((x*2)/9))+8)+(tan((2*x)^2)))
#eq = "2x+5"     #((2*x)+5)
#eq = "5!^2+sin(8+2)"    #((5!^2)+(sin(8+2)))
#eq = "sin(2)"
print "original: " + eq
parse = parseStringToList(eq)
print "parse " + str(parse)
print verify(parse)
#print parseStringToList(eq)
