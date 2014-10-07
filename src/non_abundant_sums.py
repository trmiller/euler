
def non_abundant_sums(self):
    abundant_numbers = get_non_abundant_sums(28124)
    print abundant_numbers

def is_abundant_sum(num, divisors, abundant_nums):
    count = 0
    if num % 2 == 0:
        count = count + 1
    for i in divisors:
        if i in abundant_nums:
            count = count + 1
        if count == 2:
            return False
    return True
    
def get_non_abundant_sums(top_limit):
    sum = 0
    abundant_numbers = []
    for i in xrange(1, top_limit):
        print i
        divisors = get_proper_divisors(i)
        #print divisors
        
        if is_abundant_number(i, divisors):
            #print 'abundant number'
            abundant_numbers.append(i)
        
        if is_abundant_sum(i, divisors, abundant_numbers) == True:
            sum = sum + i
        else:
            print '\tis abundant sum'
        
        #print '-------------------'
    
    #print 'all abundant nums'
    #print abundant_numbers
    return sum

def is_abundant_number(num, divisors):
    
    if sum(divisors) > num:
        return True
    return False

def get_proper_divisors(num):
    divisors = []
    
    for i in xrange(1, num):
        if num % i == 0:
            divisors.append(i)
            
    return divisors
    
if __name__ == '__main__':
    print non_abundant_sums(None)