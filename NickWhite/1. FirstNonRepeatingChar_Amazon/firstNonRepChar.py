string = "aabbbcdbbeaddf22rtep"
dic = {} #the hashmap we Use
array = [str(i) for i in string]
for i in array:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
#Now to print the first character that has only one occurrence..
for i in array:
    if dic[i] == 1:
        print(i)
        break
