# Method 1
a = int(input("enter a number "))
b = int(input("enter b number "))
for i in range(a,b+1):
    check = True
    for j in range(2,i):
        if i%j == 0:
            check = False
            break
    if check:
        print(i)

# Using for else loop
a = int(input("enter a number "))
b = int(input("enter b number "))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            print(i)