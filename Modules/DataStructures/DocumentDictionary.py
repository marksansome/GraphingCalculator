#!/usr/bin/python

#Filled in with default values
dictionary = {
    'name' : "",
    'type' : "",
    'answer' : "",
    #TODO:rename scale
    'scale' : 0.1,
    'lowerBound' : -10,
    'upperBound' : 10,
    'range' : "",
    'tableOfValues' : {
        "xValues": None,
        "yValues": None
    },
    'tree' : None,
    'isError' : ""
}

#
#   getName
#   Get the value of name in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getName(dictionary):
    return dictionary['name']

#
#   getType
#   Get the value of type in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getType(dictionary):
    return dictionary['type']

#
#   getAnswer
#   Get the value of answer in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getAnswer(dictionary):
    return dictionary['answer']

#
#   getScale
#   Get the value of scale in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getScale(dictionary):
    return dictionary['scale']

#
#   getLowerBound
#   Get the value of lower bound in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getLowerBound(dictionary):
    return dictionary['lowerBound']

#
#   getUpperBound
#   Get the value of upper bound in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getUpperBound(dictionary):
    return dictionary['upperBound']

#
#   getRange
#   Get the value of range in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getRange(dictionary):
    return dictionary['range']

#
#   getTableOfValues
#   Get the value of tableOfValues in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getTableOfValues(dictionary):
    return dictionary['tableOfValues']

#
#   getTree
#   Get the value of tree in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getTree(dictionary):
    return dictionary['tree']

#
#   getIsError
#   Get the value of isError in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getIsError(dictionary):
    return dictionary['isError']

#
#   setName
#   Sets the name value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setName(dictionary, val):
    dictionary['name'] = val

#
#   setType
#   Sets the type value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setType(dictionary, val):
    dictionary['type'] = val

#
#   setAnswer
#   Sets the answer value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setAnswer(dictionary, val):
    dictionary['answer'] = val

#
#   setScale
#   Sets the scale value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setScale(dictionary, val):
    dictionary['scale'] = val

#
#   setLowerBound
#   Sets the lower domain bound value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setLowerBound(dictionary, val):
    dictionary['lowerBound'] = val

#
#   setUpperBound
#   Sets the upper domain bound value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setUpperBound(dictionary, val):
    dictionary['upperBound'] = val

#
#   setRange
#   Sets the range value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setRange(dictionary, val):
    dictionary['range'] = val

#
#   setTableOfValues
#   Sets the table of values value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setTableOfValues(dictionary, val):
    dictionary['tableOfValues'] = val

#
#   setTree
#   Sets the tree value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setTree(dictionary, val):
    dictionary['tree'] = val

#
#   setIsError
#   Sets the isError value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setIsError(dictionary, val):
    dictionary['isError'] = val
