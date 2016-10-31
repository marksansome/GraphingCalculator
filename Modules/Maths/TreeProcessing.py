#File responsible for handling all the recursive parsing of the tree
from DataStructures import Tree
from Maths import Calculation
import numbers

tree = []

#Processing the tree and make calculations of the bottom values of the tree
def postOrderProcess(tree, root):
	#stands for not a number
	nAn = not isinstance(tree[root], numbers.Number)
	if nAn:
		#verifrying there's something to deal with at the left child
		if not tree[Tree.leftChildIndex(root)] == None:
			postOrderProcess(tree, Tree.leftChildIndex(root))
		#same for right child
		if not tree[Tree.rightChildIndex(root)] == None:
			postOrderProcess(tree, Tree.rightChildIndex(root))
	else:
		Calculation.process(tree, Tree.parentIndex(root))

#Loop to process over and over again until there's a final result
def processLoop(main):
	#TODO: PULLOP this is where I get the table
	tree = list(main)
	while not isinstance(tree[1], numbers.Number):
		postOrderProcess(tree, 1)
	return tree[1]