#!/usr/bin/python

dictionary = {
    'name' : "",
    'type' : "",
    'answer' : "",
    'scale' : "",
    'domain' : "",
    'range' : "",
    'derivative' : "",
    'integral' : "",
    'tableOfValues' : "",
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
#   getDomain
#   Get the value of domain in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getDomain(dictionary):
    return dictionary['domain']

#
#   getRange
#   Get the value of range in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getRange(dictionary):
    return dictionary['range']

#
#   getDerivative
#   Get the value of derivative in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getDerivative(dictionary):
    return dictionary['derivative']

#
#   getIntegral
#   Get the value of integral in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getIntegral(dictionary):
    return dictionary['integral']

#
#   getTableOfValues
#   Get the value of tableOfValues in the document dictionary.
#   IN: (Dictionary) the document object.
#   OUT: (String) name.
#
def getTableOfValues(dictionary):
    return dictionary['tableOfValues']

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
#   setDomain
#   Sets the domain value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setDomain(dictionary, val):
    dictionary['domain'] = val

#
#   setRange
#   Sets the range value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setRange(dictionary, val):
    dictionary['range'] = val

#
#   setDerivative
#   Sets the derivative value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setDerivative(dictionary, val):
    dictionary['derivative'] = val

#
#   setIntegral
#   Sets the intergral value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setIntegral(dictionary, val):
    dictionary['integral'] = val

#
#   setTableOfValues
#   Sets the table of values value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setTableOfValues(dictionary, val):
    dictionary['tableOfValues'] = val

#
#   setIsError
#   Sets the isError value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setIsError(dictionary, val):
    dictionary['isError'] = val
