#!/usr/bin/python

from Modules.DataStructures.DocumentDictionary import *
from Modules.Maths.Assets import *

eq = "(sin(90))"
setTree([None, 'sin', '90', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + ans  + ".", ans, 1)
