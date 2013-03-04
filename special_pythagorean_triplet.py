for a in xrange(1,800):
    for b in xrange(a+1, 700):
        for c in xrange(b+1, 800):
            if a*a + b*b == c*c:
                if a + b + c == 1000:
                    print "a = ", a, ", b = ", b , ", c = ", c
                    print a*b*c
                    break

