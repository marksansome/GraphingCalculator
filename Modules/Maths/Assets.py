from Modules.DataStructures import DocumentDictionary
from Modules.Maths import TreeProcessing
#The functions in this file are needed to "prepare" the tree from the input to the calculation process
#This includes variables managment, outputting a table working for the output as a graph and so on

#Replaces the variable named "variable" to the value "value" in the entire tree
def replaceVariables(variable, value, table):
	result = list(table)
	for i in range(len(table)):
		if table[i] == variable:
			result[i] = value
	return result

#Iterates and create a table from the low boundary to the up boundary, given the variable as a string ("x" or "y" or ..)
def iteratesDomain(tree):
	#Initialise and recovers data from the dictionnary
	domainLowBound = float(DocumentDictionary.getLowerBound())
	domainUpBound = float(DocumentDictionary.getUpperBound())
	interval = float(DocumentDictionary.getScale())
	table = tree

	#Initiating the future loop
	preimage = []
	image = []
	j = domainLowBound

	#Cause of int rounding inside "range", we need to set the last value, that's why the + 1 is there
	for i in range(int((domainUpBound - domainLowBound) / interval) + 1):
		preimage.append(j)
		#Creates a temporary copy of the table representation of the tree so we keep untouched the "main" tree with variables
		temp = replaceVariables("x", j, table)
		image.append(TreeProcessing.processLoop(temp))
		j += interval
		i += 1

	tableOfValues = {
		"xValues":preimage,
		"yValues":image
	}

	#Writing the table of values inside the global dictionary
	DocumentDictionary.setTableOfValues(tableOfValues)
	return tableOfValues

#GOOOOOOO LET'S RANCH IT UP, triggers the calculation process
def go():
	docTree = DocumentDictionary.getTree()
	#If we have a variable in the tree, it means we have to iterate on a domain
	if "x" in docTree:
		iteratesDomain(docTree)
	#If not we just expect a single number as an answer
	else:
		result = TreeProcessing.processLoop(docTree)
		DocumentDictionary.setAnswer(result)