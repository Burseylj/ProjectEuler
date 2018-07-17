#solution to project euler problem 21
from P12 import gen_divisors

divisor_sums = {}
amicables = []
for i in range(1,10000):
    divisor_sum = sum(filter(lambda x : x < i,gen_divisors(i)))
    divisor_sums[i] = divisor_sum
    if divisor_sum in divisor_sums and  i != divisor_sum:
        if divisor_sums[divisor_sum] == i:
            amicables.append(i)
            amicables.append(divisor_sum)
        
print "the sum of amicables under 10000 is {}".format(sum(set(amicables)))
