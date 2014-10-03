
def non_abundant_sums(self):
    abundant_numbers = get_abundant_sums(28123)
    print abundant_numbers
    sum = 0
    for i in xrange(12,28123):
        div = get_proper_divisors(i)
        if len(subfinder(abundant_numbers, div)) < 2:
            sum += i
    return sum

def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
    return matches
    
def get_abundant_sums(top_limit):
    abundant_numbers = []
    for i in xrange(1, top_limit):
        if is_abundant_number(i):
            abundant_numbers.append(i)
    return abundant_numbers

def is_abundant_number(num):
    divisors = get_proper_divisors(num)
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