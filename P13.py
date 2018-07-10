#Project Euler Problem 13 sol/n
#Find the first 10 digits of the sum of the 100 numbers w/ 50 digits in P13Data.txt

#We will basically just do the summation one digit at a time
def sumDigits():
    total = 0
    for i in range(49): #for each digit
        with open('P13Data.txt','r') as f:
           for line in f: # for each number in the file
               total = total + int(line[49-i]) *10**i # add this digit
               print total
               if total > 10**10: return total #stop if we have enough digits

sumDigits()
