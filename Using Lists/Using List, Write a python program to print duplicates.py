n = int(input("enter the size "))
lst1 = []
lst2 = []
for i in range(n):
    x = int(input())
    lst1.append(x)
for i in lst1:
    x = lst1.count(i)
    if (x > 1) and (i not in lst2):
        lst2.append(i)
print("the list contains duplicates ",lst2)