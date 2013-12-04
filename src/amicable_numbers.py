
def find_amicable_numbers(self):
    num_to_sum = {}
    amicable_nums = []
    amicable_sum = 0
    for i in range(1,10000):
        val = sum_divisors(i)
        if val > 1:
            num_to_sum[i] = val
    
    for i, val in num_to_sum.iteritems():
        theNum = sum_divisors(val)
        if theNum == i and i != val and val not in amicable_nums:
            amicable_nums.append(val)
    
    for i in amicable_nums:
        amicable_sum += i
        
    return amicable_sum

def sum_divisors(num):
    result = 0
    for i in range(1,num):
        if num%i == 0:
            result+= i
    return result
 
if __name__ == '__main__':
    print find_amicable_numbers(None)