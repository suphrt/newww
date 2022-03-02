a = 3789
b = (a % 1000) + 11
c = b // 100
a = (a // 1000) + b
b = a + c
print(a, b)
