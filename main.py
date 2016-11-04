#!/usr/bin/python
from Modules.Output import UI
from Modules.Output import graphing
from Modules.Maths	import Assets

#Testing replacments
table = []
for i in range(30):
	table.append("*")

for i in range(31, 100):
	table.append("x")
table[0] = None

#print Assets.replaceVariables("x", 1, table)
#print Assets.iteratesDomain("x", table)
#Assets.initialise()
Assets.iteratesDomain("x", table)
UI.UI()
