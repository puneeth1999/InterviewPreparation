
'''


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


amicalbles = []

#function that returns a list of the divisors of the number. Works great..
def find_divisors(x):
	summer = int(0)
	list_of_divisors = []
	for i in range(1, (x//2)+1):
		if(x % i == 0):
			summer += i
			list_of_divisors.append(i)
	return list_of_divisors

count_of_amicables = int(0)
for i in range(10_000):
	divisor_sum_1 = sum(find_divisors(i))
	divisor_sum_2 = sum(find_divisors(divisor_sum_1))

	if((divisor_sum_2 == i) and (divisor_sum_2<10_000) and (i<10_000) and i>divisor_sum_1):
		print('we found an amicalble pair')
		count_of_amicables += 1
		amicalbles.append(i)
		amicalbles.append(divisor_sum_1)



print('Total number of am pairs found is:', count_of_amicables)

print('The sum of amicalbles is:', sum(amicalbles))










