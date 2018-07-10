#project euler problem 4
#largest palindromic product of two three digit numbers
import math

def get_digit(number, n):
    return number // 10**n % 10
#works with digits > 2 
def is_palindrome(n):
    digits = int(math.log(n,10)) 
    for i in range(digits+1/2):
        if get_digit(n,i) != get_digit(n, digits- i):
            return False
    return True
def get_palindromes(lowest=800):
    palindromes= []
    max_prod = 1
    pair = (None,None)
    for i in range(999,lowest,-1):
        for j in range(i,lowest,-1):
            prod = i*j
            if is_palindrome(prod) and prod > max_prod:
                max_prod = prod
                pair = (i,j)
    return max_prod
