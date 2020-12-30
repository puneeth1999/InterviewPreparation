'''


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''


#Brute Force method takes forever to run. If you wanna go for Brute Force, either buy a super computer or a quantum computer.

#Let's try with sieve of eratosthenes

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    summation =0
    for p in range(n + 1): 
        if prime[p]: 
            summation = summation+p
    print(summation)

SieveOfEratosthenes(2000000) 