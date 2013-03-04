from utilities import AtkinSieve

sum_of_primes = 0
print "getting all primes"
results = AtkinSieve(2000000)

print "summing primes"
for i in results:
    sum_of_primes += i

print "-----------------"
print sum_of_primes