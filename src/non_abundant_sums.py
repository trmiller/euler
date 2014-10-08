
def problem_23(self):
    top_limit = 28123
    sieve = [False] * top_limit
    abundant_numbers = [x for x in xrange(12, top_limit) if is_abundant_number(x)]
    
    for i in xrange(len(abundant_numbers)): 
        for j in xrange(i,len(abundant_numbers)):
            if abundant_numbers[i]+abundant_numbers[j]<top_limit:
                sieve[abundant_numbers[i]+abundant_numbers[j]]=True 

    print sum([i for i in xrange(len(sieve)) if not(sieve[i])])

def is_abundant_sum(num, divisors, abundant_nums):
    count = 0
    if num % 2 == 0:
        count = count + 1
    for i in divisors:
        if i in abundant_nums:
            count = count + 1
        if count == 2:
            return True
    return False
    
def get_non_abundant_sums(top_limit, abundant_numbers):
    sum = 0
    for i in xrange(1, top_limit):
        divisors = get_proper_divisors(i)
        if is_abundant_sum(i, divisors, abundant_numbers) is False:
            print '{} is non abundant sum'.format(i)
            sum = sum + i
    
    #print 'all abundant nums'
    #print abundant_numbers
    return sum

def is_abundant_number(num):
    sum=0
    for i in xrange(1,num/2+1):
        if num%i==0:
            sum+=i
    return sum>num

def get_proper_divisors(num):
    divisors = []
    
    for i in xrange(1, num):
        if num % i == 0:
            divisors.append(i)
            
    return divisors
    
if __name__ == '__main__':
    print problem_23(None)
