from DataStructures import Tree
from Maths import TreeProcessing
#The functions in this file are needed to "prepare" the tree from the input to the calculation process
#This includes variables managment, outputting a table working for the output graph and so on
#TODO: not sure about file name?
domainLowBound = -10
domainUpBound = 10
step = 2

#Replaces the variable named "variable" to the value "value" in the entire tree
def replaceVariables(variable, value, table):
	result = list(table)
	for i in range(len(table)):
		if table[i] == variable:
			result[i] = value
	return result

#Iterates and create a table from the low boundary to the up boundary
#TODO:maybe we need to check wheter the boundaries are valid or not
def iteratesDomain(variable, table):
	image = []
	j = float(domainLowBound)
	# Cause of int rounding inside "range", we need to set the last value, that's why the + 1 is there
	for i in range(int((domainUpBound - domainLowBound) / step) + 1):
		temp = replaceVariables(variable, j, table)
		image.append(TreeProcessing.processLoop(temp))
		j += step
		i += 1

	#TODO:write in the dic
	return image
