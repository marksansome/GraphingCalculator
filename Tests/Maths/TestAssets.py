from DataStructures import Tree
from Maths import Assets

#Testing replacments
table = []
for i in range(30):
	table.append("+")

for i in range(31, 100):
	table.append("x")
table[0] = None

#print Assets.replaceVariables("x", 1, table)
print Assets.iteratesDomain("x", table)


