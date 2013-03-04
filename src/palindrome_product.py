def isEven(num):
    if num % 2 == 0:
        return True
    return False

def isPalindrome(num):
    numAsString = str(num)
    length = len(numAsString)
    if length < 3:
        return False
    middle = int(length/2)
    for i in range(0, middle):
        if numAsString[i] != numAsString[length-i-1]:
            return False
    return True
    
a = []
palindromes = {}
largest_palindrome = 0
for i in range(1,1001):
    a.append(i)
    
for i in range(0,len(a)-1):
    for j in range(0, len(a)-1):
        #print a[i], " * ", a[j]
        result = a[i] * a[j]
        if isPalindrome(result):
            if not palindromes.has_key(result):
                palindromes[result] = 0
            if result > largest_palindrome:
                largest_palindrome = result;

print "-------------------"
for i in sorted(palindromes.iterkeys()):
    print i

print "-------------------"
print a[len(a)-1]
print "largets palindrome = ", largest_palindrome
            