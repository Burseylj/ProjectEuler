#Project Euler Problem 13 sol/n
#Find the first 10 digits of the sum of the 100 numbers w/ 50 digits in P13Data.txt

numbers = open('P13Data.txt').read().splitlines()

numbers = map(long,numbers)
print sum(numbers)
