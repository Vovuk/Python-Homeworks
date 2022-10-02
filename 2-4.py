n = int(input('Input n: '))

a = []
b = []
for i in range(-n, n+1):
    a.append(i)
print(a)
f = 'file.txt'
data = open(f, 'r')

s = 1
for line in data:
    s *= a[int(line)]
print(s)
