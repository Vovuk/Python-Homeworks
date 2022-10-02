n = int(input('Input n:'))
summ = 0
a = []
for i in range(1, n+1):
    a.append((1+1/i)**i)
print(round(sum(a), 2))
