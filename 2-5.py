import random
a = [int(i) for i in input("Input list: ").split()]
print(a)
for i in range(len(a)):
    j = random.randint(0, len(a)-1)
    el = a.pop(j)
    a.append(el)
print(a)
