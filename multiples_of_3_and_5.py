class Multiples:
	nums = [3,5]
	upper_limit = 1000
	
	result = 0
	
	for i in range(1,upper_limit):
		if i%3 == 0 or i%5 == 0:
			result += i
	
	print result