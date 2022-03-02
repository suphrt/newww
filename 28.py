a = []
b = []
for m in range(101):
    a.append(300 - m*100)
for n in range(101):
    b.append(a[n]+200)
    
c = 0
for a in b:
    if a < 0:
        c+=1
print(c)
