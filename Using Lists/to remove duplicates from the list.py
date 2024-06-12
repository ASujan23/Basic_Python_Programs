n = int(input("enter the size: "))
lst1 = []
for i in range(n):
    x = int(input())
    lst1.append(x)
    lst2 = []
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print("the list after remove duplicates ",lst2)

# another way
"""
n = int(input("enter the size: "))
lst1 = []
for i in range(n):
    x = int(input())
    lst1.append(x)

for i in lst1:
    x = lst1.count(i)
    if x > 1:
        lst1.remove(i)
print("the list after remove duplicates ",lst1)
"""