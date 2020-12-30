
numbers = [x for x in range (1,28124)]

def total_of_the_divisors(x):
	summer = int(0)
	list_of_divisors = []
	for i in range(1, (x//2)+1):
		if(x % i == 0):
			summer += i
			list_of_divisors.append(i)
	total = sum(list_of_divisors)
	return total


#Get the list of all abundant numbers less than 28124
list_of_abundant_numbers = []
for i in range(1, 28124):
	s = total_of_the_divisors(i)
	if(s > i):
		list_of_abundant_numbers.append(s)



# Python program to print all  
# sublist from a given list  
  
# function to generate all the sub lists 
def sub_lists(list1): 
  
    # store all the sublists  
    sublist = [[]] 
      
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j]
            if(sum(sub)<= 28123):
            	sublist.append(sum(sub))

             
              
      
    return sublist

print(sub_lists(list_of_abundant_numbers))