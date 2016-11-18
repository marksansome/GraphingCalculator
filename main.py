#!/usr/bin/python
import sys
from Modules.Output.UI import *
from Modules.Maths.Assets import *
from Modules.DataStructures.DocumentDictionary import *

if len(sys.argv) == 2:
    with open(sys.argv[1],'r') as myFile:
        for line in myFile:
            print line
else:
    UI()
