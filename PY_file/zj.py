f = 1
g = 1
day=input()
day=int(day)
for i in range(1,day,1):
    f+=(i+1)
    g+=f
print(f)
print(g)
