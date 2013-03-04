from utilities import isprime

target = 10001
primes = {}
i = 7919
num_primes = 1000

while True:
    if isprime(i):
        primes[num_primes] = i
        num_primes += 1
        if num_primes == target + 1:
            print i
            break
    i += 1
