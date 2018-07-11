#attempt at project euler problem 14





def collatzLength(x):
    initialValue = x
    length = 0
    while x != 1:
        if knownLengths[x-1] != -1:
            length += knownLengths[x-1]
            break
        else :
           # knownLengths[x-1] = collatzLength(collatzSequence(x))
            x = collatzSequence(x)
            length += 1
            
    knownLengths[initialValue-1] = length
    return length +1





def collatzSequence(x):
    if x == 1:
        return 1
    if x & 1:
        return (3*x +1)
    else:
        return (x/2)

knownLengths = [-1]*1000000
for i in range(1,1000):
    print "length of ",i,"=",collatzLength(i)
