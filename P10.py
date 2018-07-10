#Project Euler 10
#Find the sum of primes under two million
from P7 import is_prime

sum = 2
for i in range(3,2000000,2):
    if is_prime(i):
        sum += i

print sum
