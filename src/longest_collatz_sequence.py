def getCollatzSequence(num):
    result = num
    count = 1
    while result > 1:
        if result % 2 == 0:
            result = result / 2
        else:
            result = result * 3 + 1
        count += 1
    return count

collatz_nums = {}
max_count = 0
max_collatz = 0
for i in xrange(13,1000000):
    sequence_count = getCollatzSequence(i)
    print i, " has chain of ", sequence_count
    if sequence_count > max_count:
        max_count = sequence_count
        max_collatz = i

print "--------------------"
print max_collatz, " with ", max_count, " chain"
    