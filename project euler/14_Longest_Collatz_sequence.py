
'''


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''



max_length = 0
for i in range(1,1000000+1):
	counter = 0
	number = i
	# print('updated number',number)
	# print('current number:',number)
	while(number != 1):
		
		
		if(number%2 == 0):
			number = number / 2
			counter += 1
		else:
			number = (3*number) + 1
			counter += 1
	
	#print('presently i is:', i)
	if(counter > max_length):
		max_length = counter
		print('current__________ max____________length',max_length,'\n','current__________number', i)
		
