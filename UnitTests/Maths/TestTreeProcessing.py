from Modules.DataStructures import Tree
from Modules.Maths import TreeProcessing
#testing singles cases of TreeProcessing

#tests for 30 additions of 30 2
for i in range(30):
	Tree.table.append("+")

for i in range(31, 61):
	Tree.table.append(2)
Tree.table[0] = None



print "Result: " + str(TreeProcessing.processLoop(Tree.table)) + "\n\n"

#tests
Tree.table = []
for i in range(30):
	Tree.table.append(None)

Tree.table.insert(1,"+")
Tree.table.insert(2,"sin")
Tree.table.insert(3, 3)
Tree.table.insert(4, 0.5)


print "Result: " + str(TreeProcessing.processLoop(Tree.table))
