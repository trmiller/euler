from utilities import *

size = 21
lattice = [[0 for i in xrange(size)] for i in xrange(size)]

#@memoize
def getPathsFromCurrent(patha, pathb):
    i = 0
    realLimit = size - 1
    if patha == realLimit and pathb == realLimit:
        return 1
    if lattice[patha][pathb] != -1:
        return lattice[patha][pathb]
    if patha != realLimit:
        i += getPathsFromCurrent(patha + 1, pathb) 
    if pathb != realLimit:
        i += getPathsFromCurrent(patha, pathb + 1)
    lattice[patha][pathb] = i
    return i
        

for i in xrange(0, size):
    for j in xrange(0, size):
        lattice[i][j] = -1

countOfPaths = getPathsFromCurrent(0,0)

print "Paths = ", countOfPaths