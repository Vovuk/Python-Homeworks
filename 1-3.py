x = int(input('Input x: '))
y = int(input('Input y: '))
if y == 0 or x == 0:
    print('error')
else:
    if x > 0 and y > 0:
        print('1 quarter')
    elif x < 0 and y > 0:
        print('2 quarter')
    elif x < 0 and y < 0:
        print('3 quarter')
    else:
        print('4 quarter')
