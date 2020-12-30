


'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''
import math
number = int(math.pow(2, 1000))

string = str(number)

sum = 0

for i in range(len(string)):
	sum += int(string[i])
print(sum)