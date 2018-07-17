#attempt at project euler problem 14


#for some reason the dynamic programming parts aren't helping

import time
 
start = time.time()

def collatzLength(x):
    initialValue = x
    length = 0
    while x != 1:
        x = collatzSequence(x)
        length+= 1

    return length +1





def collatzSequence(x):
    if x & 1:
        return (3*x +1)
    else:
        return (x/2)


biggest = 0

for i in range(1,1000000):
    clt = collatzLength(i)
    if clt > biggest:
        biggest = clt
        starting = i

elapsed = (time.time() - start)
print "found starting number %s with length %s in %s seconds" % (starting,biggest,elapsed)
        
