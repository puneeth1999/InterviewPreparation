'''


.A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
sum = 1000

for a in range(sum//3):
	for b in range(sum//2):
		c = sum-a-b
		if(a*a + b*b == c*c):
			print('a =', a)
			print('b =', b)
			print('c =', c)
			print('a*b*c =',a*b*c)