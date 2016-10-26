from Global import Tree
from Maths import TreeProcessing

#tests for 30 additions of 30 2
for i in range(30):
	Tree.table.append("+")

for i in range(31, 61):
	Tree.table.append(2)
Tree.table[0] = None

TreeProcessing.processLoop()

print "Result: " + str(Tree.getAtIndex(1))
print "Iteration Amount: " + str(Tree.iterationAmount)

#tests