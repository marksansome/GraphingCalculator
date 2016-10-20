#!/usr/bin/python

#   ASCII Colour Table
GREEN = '\033[92m'
ERROR = '\033[91m'

HEADER = '\033[95m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

ENDC = '\033[0m'

#
#   testResults
#   Hash table storing the number of successful and failed tests.
#
testResults = {
    'passed':0,
    'failed':0
}

def printResults():
    print "Tests Passed: " + GREEN  + str(testResults['passed']) + ENDC
    print "Tests Failed: " + ERROR  + str(testResults['failed']) + ENDC

#
#   assertTrue
#   Make an assertion that a given value will return true.
#   IN: (String) assertion to make, (Boolean) assertion status.
#   OUT: (Boolean) status of assertion.
#
def assertTrue(asrt, stmt):
    if (stmt == True):
        printPass(asrt)
        return True
    else:
        printFailure(asrt)
        return False

#
#   assertFalse
#   Make an assertion that a given value will return false.
#   IN: (String) assertion to make, (Boolean) assertion status.
#   OUT: (Boolean) status of assertion.
#
def assertFalse(asrt, stmt):
    if (stmt == False):
        printPass(asrt)
        return True
    else:
        printFailure(asrt)
        return False

#
#   assertEqual
#   Make an assertion that two given values will be equal.
#   IN: (String) assertion to make, (void) some value to compare, (void) comparison value.
#   OUT: (Boolean) status of assertion.
#
def assertEqual (asrt, stmt, other):
    if (stmt == other):
        printPass(asrt)
        return True
    else:
        printFailure(asrt)
        return False

#
#   assertNotEqual
#   Make an assertion that two given values will not be equal.
#   IN: (String) assertion to make, (void) some value to compare, (void) comparison value.
#   OUT: (Boolean) status of assertion.
#
def assertNotEqual (asrt, stmt, other):
    if (stmt != other):
        printPass(asrt)
        return True
    else:
        printFailure(asrt)
        return False

#
#   printPass
#   Print an assertion status mesage. Prints tests with colour.
#   IN: (String) assertion made.
#   OUT: Print Statement
#
def printPass(asrt):
    testResults['passed'] += 1
    print "The assertion: " + asrt + " - test" + GREEN + " Passed" + ENDC

#
#   printFailure
#   Print an assertion status mesage. Prints tests with colour.
#   IN: (String) assertion made.
#   OUT: Print Statement
#
def printFailure(asrt):
    testResults['failed'] += 1
    print "The assertion: " + asrt + " - test" + ERROR + " Failed" + ENDC
