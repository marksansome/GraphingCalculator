from Global import Tree
#The functions in this file are needed to "prepare" the tree from the input to the calculation process
#This includes variables managment, outputting a table working for the output graph and so on
#TODO: not sure about file name?
domainLowBound = 0
domainUpBound = 100
step = 1

#Replaces the variable named "variable" to the value "value" in the entire tree
def replaceVariables(variable, value):
	for i in Tree.table:
		if Tree.getAtIndex(i) == variable:
			Tree.setAtIndex(i, value)

