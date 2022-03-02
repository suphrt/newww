x = 4
y = 132
t = x % y
x = x + t + 15
y = y // x
t = t + y
print(t, x, y)
