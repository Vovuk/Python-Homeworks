from math import sqrt, pow
x1 = int(input('Input x1: '))
y1 = int(input('Input y1: '))
x2 = int(input('Input x2: '))
y2 = int(input('Input y2: '))

if x1 == x2 and y1 == y2:
    print('error')
else:
    distance = sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
    print("%4.2f" % distance)
