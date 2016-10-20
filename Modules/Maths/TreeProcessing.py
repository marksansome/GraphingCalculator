#File responsible for handling all the recursive parsing of the tree
from Global import Tree
from Maths import Calculation
import numbers

#postOrder processing of the tree
def postOrderProcess(root):
	#stands for not a number
	nAn = not isinstance(root, numbers.Number)
	if nAn:
		postOrderProcess(Tree.leftChildIndex(root))
		postOrderProcess(Tree.rightChildIndex(root))
	else:
		Calculation.process(root)