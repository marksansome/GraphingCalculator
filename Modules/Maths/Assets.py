from Global import Tree
#The functions in this file are needed to "prepare" the tree from the input to the calculation process
#This includes variables managment, outputting a table working for the output graph and so on
#TODO: not sure about file name?
domainLowBound = 0
domainUpBound = 100
step = 1

#Replaces the variable named "variable" to the value "value" in the entire tree
def replaceVariables(variable, value, table):
	result = list(table)
	for i in range(len(Tree.table)):
		if table[i] == variable:
			result[i] = value
	return result

#Iterates and create a table from the low boundary to the up boundary
#TODO:maybe we need to check wheter the boundaries are valid or not
def iteratesDomain():
	resultTable = []
	for i in range((domainUpBound - domainLowBound) / step):
		#resultTable.append[]
		i += 1
