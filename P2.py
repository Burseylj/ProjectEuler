# By Louis Bursey
# Intended to solve Problem 2 from ProjectEuler.net
# Sum the even terms of the Fibonacci Sequence that do not exceed 4 million
# (Starting with (1,2)


#
# F(1) = 1 and F(2) = 2. Since F(1) is odd and F(2) is even, F(3) is odd.
# F(4) = F(2) + F(3), so it is also odd
# F(5) = F(3) + F(4), so it is even. We see a pattern here: F(2 + 3n) is even
# for all n.
#
# Not sure how to use this information... Could use the formula found at:
# https://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding
# However, I'm not convinced that computing n/3 powers of phi will be much more efficient
# than just doing n additions... also the FP error will be unsightly
# we'll see, I guess

# math.floor((phi**12)/2 + 0.5)

# Yep, this is disasterously divergent. Let's just brute force this thing
import timeit

def naive_solution():
    a = 1
    b = 2
    c = 0
    total = b 
    while (a+b) <= 4000000: # 4 million
        c = a
        a = b
        b = c + b
        if (b%2 ==0):
            total = total +b
    return total
 
# Actually, the even terms are related by the recursive relation:
# E(n) = 4*E(n-1) + E(n-2)
# pf. in pdf

def clever_solution():
    a = 2
    b = 8
    c = 0
    total = a + b 
    while (a+4*b) <= 4000000: # 4 million
        c = a
        a = b
        b = 4*b + c
        if (b%2 ==0):
            total = total +b
    return total

print "Naive solution", naive_solution()
print "timeit results:", timeit.timeit(naive_solution) 
print "Clever solution", clever_solution()
print "timeit results:", timeit.timeit(clever_solution)

# So this solution is faster for sure. Cool.
