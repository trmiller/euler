class FibonacciSum:
    upper_limit = 4000000
    current = 1
    previous = 1
    result = 2
    i = 2
    
    while current < upper_limit:
        current = previous + i
        if current < upper_limit:
            previous = i
            print current 
            if current % 2 == 0:
                print "\t even fibonacci"
                result += current
            i = current
    
    print "result is %d" % (result)
