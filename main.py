#!/usr/bin/python
from Modules.Output import UI
from Modules.Maths import Assets
from Modules.DataStructures import DocumentDictionary

#TODO:remove that shit
#Testing replacements with a temporary table for RANCHING FUSION
table = []
for i in range(20):
	table.append("*")

for i in range(31, 100):
	table.append("x")
table[0] = None

#DocumentDictionary.setTree(DocumentDictionary.dictionary, table)
Assets.iteratesDomain("x",table)

UI.UI()
