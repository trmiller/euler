import math

class LargestPrimeFactor:
    target = 600851475143
    upper_limit = int(math.sqrt(target))
    #target = 600851475143
    largest_prime = 0
    for i in range(1, upper_limit+1):
        if target % i == 0:
            #print i, " is a factor of ", target
            for div in range(2, (i/2)+1):
                if i%div==0:
                    break
            else:
                largest_prime = i
                #print "\t PRIME"
                
    print "--------------------------------"
    print largest_prime, " is the largest prime factor of ", target