##project euler problem 12
import math

def triangular_number(n):
    return n * (n + 1) // 2 


def gen_divisors(n):
    divisors = []
    for i in xrange(1, int(math.sqrt(n) +1)):
        if n % i == 0:
            yield i
            if i*i != n:
                yield n/i
def main():
    n = 1
    i = 1
    div = 0
    div_limit = 500
    while(div < div_limit):
        i += 1
        n+=i
        div = len(list(gen_divisors(n)))

    print "with {} divisors, the {}th triangular number {} has the most.".format(div,i,n)
