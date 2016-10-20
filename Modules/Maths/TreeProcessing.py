#File responsible for handling all the recursive parsing of the tree
from Global import Tree
from Maths import Calculation
import numbers

#postOrder processing of the tree
def postOrderProcess(root):
	#stands for not a number
	nAn = not isinstance(Tree.getAtIndex(root), numbers.Number)
	if nAn:
		#verifrying there's something to deal with empty slots
		if not Tree.getAtIndex(Tree.leftChildIndex(root)) == None:
			postOrderProcess(Tree.leftChildIndex(root))

		#same for right child
		if not Tree.getAtIndex(Tree.rightChildIndex(root)) == None:
			postOrderProcess(Tree.rightChildIndex(root))
	else:
		Calculation.process(Tree.parentIndex(root))