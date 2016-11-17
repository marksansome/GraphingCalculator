#!/usr/bin/python

from Testing import *
from Modules.Maths.FillTree import *

#
#   Verify Driver
#   Verify the functions within verifier
#
printHeader("Fill Tree Driver", "Testing functions in FillTree: parseString.")

eq = "((2*x)+5)"
parseString(eq)
ans = [None, '+', '*', '5', '2', 'x', None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " yields " + str(ans), ans, ansList)
