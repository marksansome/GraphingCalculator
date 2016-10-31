from Global import Tree
from Maths import Assets

Tree.table = []
for i in range(30):
	Tree.table.append("x")

Assets.replaceVariables("x", 2)

print Tree.table
