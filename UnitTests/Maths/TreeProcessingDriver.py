#!/usr/bin/python
from Testing import *
from Modules.DataStructures.DocumentDictionary import *
from Modules.Maths.TreeProcessing import *

#
#   Verify Driver
#   Verify the functions within verifier
#
printHeader("Math Processing Driver", "Testing functions mathematical processing functions.")

eq = "(sin(pi))"
setTree([None, 'sin', 'pi', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, 1)
