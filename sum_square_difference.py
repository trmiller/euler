count = 101
sum_squares = 0
square_sum = 0
sums = 0

for i in xrange(0, count):
    sums += i
    sum_squares += (i*i)

square_sum = sums*sums

result = square_sum - sum_squares
print square_sum, " - ", sum_squares, " = ", result
