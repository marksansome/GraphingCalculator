from DataStructures import Tree
from Maths import Assets

#Testing replacments
Tree.table = []
for i in range(30):
	Tree.table.append("x")

print Assets.replaceVariables("x", 2, Tree.table)


