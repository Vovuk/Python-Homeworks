a = int(input('Input number quarter: '))
if a not in [1, 2, 3, 4]:
    print('error')
else:
    if a == 1:
        print('x = (0, +∞), y = (0, +∞)')
    elif a == 2:
        print('x = (-∞, 0), y = (0, +∞)')
    elif a == 3:
        print('x = (-∞, 0), y = (-∞, 0)')
    else:
        print('x = (0, +∞), y = (-∞, 0)')
