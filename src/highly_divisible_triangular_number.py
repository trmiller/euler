import math

def getFactorCount(num):
    count = 0
    root = long(math.sqrt(num))
    for i in xrange(1,root + 1):
        if num % i == 0:
            count += 2
    if root * root == num:
        count =- 1
        
    return count

factorCount = 0
i = 1
triangle = 0
while True:
    triangle += i
    factorCount = getFactorCount(triangle)
    print triangle, " - ", factorCount
    if factorCount >= 500:
        print "winner winner chicken dinner"
        break
    i += 1
print "done" 