power = 1000
num = 2 ** power
numAsStr = str(num)
the_sum = 0
for i in numAsStr:
    curr = int(i)
    the_sum += curr

print the_sum