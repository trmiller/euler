num_to_letters = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
ten_to_letters = {0:"", 10:"", 20: "twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
count = 0
curr_ten = 10
curr_hundred = 0
curr_thousand = 0
for i in xrange(1, 1000):
    num = i
    word = ""
    
    if i % 10 == 0:
        if i > 10 :
            curr_ten += 10
    
    if i >= 100:
        if i % 100 == 0:
            curr_hundred += 1
            curr_ten = 0
        
        word += num_to_letters[curr_hundred] + "hundred"
        
        if i % 100 != 0:
            word += "and"
        
    if curr_ten >= 20:
        num -= ((curr_hundred*100) + curr_ten) 
    else:
        num -= (curr_hundred * 100)
    
    word += ten_to_letters[curr_ten] + num_to_letters[num]
    print word
    count += len(word)

word = "onethousand"
print word
count += len(word)
print count
    