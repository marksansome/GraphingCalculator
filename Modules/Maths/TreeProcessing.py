#File responsible for handling all the recursive parsing of the tree
from Global import Tree
from Maths import Calculation
import numbers

tree = []

#Processing the tree and make calculations of the bottom values of the tree
def postOrderProcess(tree, root):
	#stands for not a number
	nAn = not isinstance(Tree.getAtIndex(root), numbers.Number)
	if nAn:
		#verifrying there's something to deal with at the left child
		if not Tree.getAtIndex(Tree.leftChildIndex(root)) == None:
			postOrderProcess(Tree.leftChildIndex(root))
		#same for right child
		if not Tree.getAtIndex(Tree.rightChildIndex(root)) == None:
			postOrderProcess(Tree.rightChildIndex(root))
	else:
		Calculation.process(Tree.parentIndex(root))

#Loop to process over and over again until there's a final result
def processLoop():
	tree = list(Tree.table)
	while not isinstance(tree[1], numbers.Number):
		postOrderProcess(tree, 1)
	return Tree.getAtIndex(1)