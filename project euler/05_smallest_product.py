'''
.2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


'''
ANS:

If we carefully observe, the answer is nothing but the LCM of all the given numbers


ans = LCM(ans, i) 
         = ans * i / gcd(ans, i) [Using the below property,
                                 a*b = gcd(a,b) * lcm(a,b)]

'''

#To find the LCM:
import fractions

def findLCM(n):
	lcm = 1
	for i in range(1, n+1):
		lcm = (lcm * i)/fractions.gcd(lcm, i)
	return lcm

number = int(input('enter the number: '))

print('The required number is:',findLCM(number))



