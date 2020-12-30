a = [1,2,3,2,1,4] #It should return 2 and not 1
#Initialise a dictionary/HashMap
dict = {}
for i in range(len(a)):
    if a[i] in dict:
        print(a[i])
        break
    else:
        dict[a[i]] = 1
