#File responsible for handling all the recursive parsing of the tree
from Global import Tree
from Maths import Calculation
import numbers

#Processing the tree and make calculations of the bottom values of the tree
def postOrderProcess(root):

	#TODO:remove this?
	#Counting the iterations to make sure we do not overlap
	Tree.iterationAmount += 1
	#stands for not a number
	nAn = not isinstance(Tree.getAtIndex(root), numbers.Number)

	if nAn:
		#verifrying there's something to deal with at the left child
		if not Tree.getAtIndex(Tree.leftChildIndex(root)) == None:
			#TODO:scope testing
			print str(root) + " left " + str(Tree.leftChildIndex(root))
			postOrderProcess(Tree.leftChildIndex(root))
		#same for right child
		if not Tree.getAtIndex(Tree.rightChildIndex(root)) == None:
			#TODO:scope testing
			print str(root) + " right " + str(Tree.rightChildIndex(root))
			postOrderProcess(Tree.rightChildIndex(root))
	else:
		Calculation.process(Tree.parentIndex(root))
	#TODO:scope testing
	print Tree.table

#Loop to process over and over again until there's a final result
def processLoop():
	while not isinstance(Tree.getAtIndex(1), numbers.Number):
		postOrderProcess(1)