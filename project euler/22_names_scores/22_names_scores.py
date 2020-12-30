'''


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''





file = open('names.txt', 'r')
result = file.read()

names = result.split(",")

cleaned_names = []
for name in names:
	cleaned_names.append(name[1:-1])

names = cleaned_names
names.sort()

#	print(names)

alphabets = ['A','B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

name = 'COLIN'

index_of_the_name = (names.index('COLIN'))+1

# ###########################################################
# summer = 0
# for letter in name:
	
# 	# print(letter)
# 	index_of_the_letter = alphabets.index(letter)+1
# 	# print(index_of_the_letter)
# 	summer += index_of_the_letter
# print('name =',name)
# print('summer =',summer)
# print('index_of_the_name =', index_of_the_name)
# print(summer*index_of_the_name)
###########################################################


totals = []
index_of_the_name = 0
for name in names:
	index_of_the_name = names.index(name)+1
	summer = 0
	for letter in name:
		
		# print(letter)
		index_of_the_letter = alphabets.index(letter)+1
		# print(index_of_the_letter)
		summer += index_of_the_letter
	score = summer*index_of_the_name
	totals.append(score)
	print('name =',name)
	print('summer =',summer)
	print('index_of_the_name =', index_of_the_name)
	print(summer*index_of_the_name)
	print('\n\n\n')


# # print(names[:10])

# print(total)

# print(names.index('COLIN'))

print(sum(totals))