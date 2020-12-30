'''

.The sum of the squares of the first ten natural numbers is,
12+22+...+102=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



'''



import math
number  = int(input('Enter the number:'))

#SumOfSquares
sum_of_squares = 0
for i in range(1, number+1):
	sum_of_squares = sum_of_squares + math.pow(i, 2)
#print(sum_of_squares)


#SquareOfSums

basic_sum = 0
for i in range(1, number+1):
	basic_sum += i
square_of_sums = math.pow(basic_sum, 2)
#print(square_of_sums)
#print('\n')

result = square_of_sums - sum_of_squares


print('Your answer is:',result)