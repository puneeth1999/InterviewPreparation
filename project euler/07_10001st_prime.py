
'''


.By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''





n = int(input('Enter : '))
prime_numbers = [2,3]
i=3
if(0<n<3):
    print(n,'th Prime Number is :',prime_numbers[n-1])
elif(n>2):
    while (True):
        i+=1
        status = True
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                status = False
                break
        if(status==True):
            prime_numbers.append(i)
        if(len(prime_numbers)==n):
            break
    print(n,'th Prime Number is :', prime_numbers[n-1])
else:
    print('Please Enter A Valid Number')


