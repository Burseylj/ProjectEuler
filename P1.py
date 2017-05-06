#By Louis Bursey
#Program to solve Problem 1 from EulerProject.net
#
#Find the sum of all the multiples of 3 or 5 below 1000.

#This solution is the most obvious, however it takes 2*1000 compares ops.
def naive_solution():
    sum = 0;
    for n in range(1000):
        if (n % 3) == 0 or (n % 5) == 0:
            sum = sum + n

    return sum

print naive_solution()

#Better solution by doing SumDivBy(3) + SumDivBy(5) - SumDivBy(15) to
#get sol/n in 9/15*1000 operations, I don't feel like coding this right now
