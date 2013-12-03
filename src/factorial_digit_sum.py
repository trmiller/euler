import math

def factorial_digit_sum(self):
    factorial = math.factorial(100)
    factorial_sum = 0
    for i in str(factorial):
        factorial_sum += int(i)
    
    return factorial_sum

if __name__ == '__main__':
    print factorial_digit_sum(None)