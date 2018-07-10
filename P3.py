# By Louis Bursey
# Program to solve Problem 3 from ProjectEuler.net
# What is the largest prime factor of the number 600851475143 ?
from math import floor,sqrt
from itertools import count, islice
number = 600851475143






#naive_solution(number)


def reduce_number(num, p):
    while (num % p == 0):
        num = num/p
    return num

def naive_solution(num):
    pn_bound = num
    p = 2
    pn_bound = reduce_number(pn_bound, 2) # in case num is even
    p +=1
    # we don't need to check if p is prime. if p is not prime, p is a product of
    # some smaller primes, which will have already been divided out, so p will not
    # divide pn_bound. we can therefore assume p is prime if it divides pn_bound
    while(p <= num): 
        if (pn_bound % p == 0):
            pn_bound = reduce_number(pn_bound, p)
            if (pn_bound == 1):
                return p
        p +=2


print naive_solution(number)
        
        
