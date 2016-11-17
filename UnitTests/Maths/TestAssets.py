from Modules.Maths import Assets
from Modules.DataStructures import DocumentDictionary

#Testing replacments
table = []
for i in range(0,30):
	table.append("+")

for i in range(31, 100):
	table.append("x")
table[0] = None

DocumentDictionary.setTree(table)
print Assets.iteratesDomain("x", table)
