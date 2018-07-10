#Project Euler problem 5
#find 10,001st prime
from math import sqrt, floor
from itertools import count, islice

#updated, now a decent prime checker
def is_prime(n):
    if n < 2: return False # these are not prime
    elif n < 4: return True # 2,3 are prime
    elif n % 2 == 0: return False #prime is not even
    elif n < 9: return True #already discluded 
    elif n % 3 ==0 :return False #if divisible by 3
    else :
        bound = floor(sqrt(n))

        #because all primes are of form 6k+-1, we can do this 
        for f in islice(count(5,6), (int(sqrt(n)) + 1 )//6):
            if n % f == 0 : return False
            if n % (f+2) == 0 :return False
        return True

def nth_prime(n):
    if n < 1 :
        return 0
    elif n == 1:
        return 2
    else:
        primecount = 1
        i = 1
        while primecount < n:
            i +=2
            if is_prime(i):
               
                primecount+= 1
            
        return i

#print nth_prime(10001)

