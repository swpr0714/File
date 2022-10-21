odd = int(input("請輸入奇數(>2):"))
upper = int(odd/2)
print((upper)*" ", end="")
print("*")
interval = 1
for i in range(upper,0,-1):
    print((i-1)*" ", end="")
    print("*", end="")
    print(interval*" ", end="")
    print("*")
    interval += 2
interval -= 2
for i in range(1,upper,1):
    interval -= 2
    print(i*" ", end="")
    print("*", end="")
    print(interval*" ", end="")
    print("*")
print(upper*" "+"*")
