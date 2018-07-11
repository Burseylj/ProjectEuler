##getting background info for project euler problem 12

triangle = 1
order = 1

while (triangle < 2**500):
    triangle = +order
    order += 1
    print "order = 1 , number = " + triangle
