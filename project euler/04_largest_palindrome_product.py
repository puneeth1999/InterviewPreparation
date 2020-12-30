'''


.A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


'''
TESTING
'''
# number = 909909

# if(str(number) == str(number)[::-1]):
# 	print('Plaindrome')
# else:
# 	print('Not a palindrome')

max_palindrome = 0
for i in range (100, 1000):
	for j in range(100, 1000):
		number = str(i*j)
		if(str(number) == str(number)[::-1]):
			if(int(number)>int(max_palindrome)):
				max_palindrome = number
print(max_palindrome)