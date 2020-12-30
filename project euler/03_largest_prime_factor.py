'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# for i in range(600851475143, 0, -1):
# 	if()

# number = int(600851475143)

# if number > 1:
# 	for i in range(2, number):
# 		if (number%i == 0):
# 			print('This is not a prime number!')
# 			break
# 		else:
# 			print('This is a prime number!')
# else:
# 	print('This is not a prime number!')



import math

maxPrimeNumber = -1
n = 600851475143

# while n%2 == 0:
# 	maxPrimeNumber = n
# 	n = n/2

for i in range(2, (int(math.sqrt(n)) + 1), 1): 
    while n % i == 0: 
        maxPrimeNumber = i 
        n = n / i 
  

if n > 2: 
    maxPrime = n 
  
print(maxPrimeNumber)

