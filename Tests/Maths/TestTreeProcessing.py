from Global import Tree
from Maths import TreeProcessing
#testing singles cases of TreeProcessing

#tests for 30 additions of 30 2
for i in range(30):
	Tree.table.append("+")

for i in range(31, 61):
	Tree.table.append(2)
Tree.table[0] = None

TreeProcessing.processLoop()

print "Result: " + str(Tree.getAtIndex(1))
print "Iteration Amount: " + str(Tree.iterationAmount) + "\n\n"

#tests
Tree.table = []
for i in range(30):
	Tree.table.append(None)
print Tree.table
Tree.table.insert(1,"+")
Tree.table.insert(2,"sin")
Tree.table.insert(3, 3)
Tree.table.insert(4, 0.5)
print Tree.table

TreeProcessing.processLoop()

print "Result: " + str(Tree.getAtIndex(1))
print Tree.table


