#!/usr/bin/python

from Testing import *
from Modules.Input.Verifier import *

#
#   Verify Driver
#   Verify the functions within verifier
#
printHeader("Verifier Driver", "Testing functions in verifier: verify, parseStringToList.")

#
#   Section one - Test Verify
#
printSectionHeader("Test Verify", "Test possible branch cases of the parsing functions.")

eq = "2x+5"
ans = "((2*x)+5)"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "5.25+6*7-9/1"
ans = "((5.25+(6*7))-(9/1))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "sin(2)"
ans = "(sin(2))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "sin(2+1)"
ans = "(sin(2+1))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "(1+2)^3*4"
ans = "(((1+2)^3)*4)"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "5!^2+sin(8+2)"
ans = "((5!^2)+(sin(8+2)))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "(2+(3/9))*2"
ans = "((2+(3/9))*2)"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "(2+3)*4+(5/9)"
ans = "(((2+3)*4)+(5/9))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "(2+(3/9))*2+(2+4)+8"
ans = "((((2+(3/9))*2)+(2+4))+8)"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "17-2*3+7"
ans = "((17-(2*3))+7)"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "(1^(3+2))^2+(4+9)"
ans = "(((1^(3+2))^2)+(4+9))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "2*sin(cos(tanh(1+2/3*4-5-6)))"
ans = "(2*(sin(cos(tanh(((1+((2/3)*4))-5)-6)))))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "sin(2) + sin(4+2)"
ans = "((sin(2))+(sin(4+2)))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "2*sin(cos(tanh(1+2/3*4-5-6)))+(2+(arctanh(456+876-987654321)))"
ans = "((2*(sin(cos(tanh(((1+((2/3)*4))-5)-6)))))+(2+(arctanh((456+876)-987654321))))"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)

eq = "(2+4)! + 2"
ans = "(((2+4)!)+2)"
preParse = parseStringToList(eq)
ansVerified = verify(preParse)
assertEqual("The equation " + eq + " is equal to " + ans + ".",ansVerified,ans)
