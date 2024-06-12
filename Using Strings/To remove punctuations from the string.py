a = input("enter the string: ")
b = ""
for i in a:
    if(i >= "a" and i<="z") or (i >= "A" and i<="Z") or (i>="0" and i<="9"):
        b = b+i
print(b)
#Another Method
"""
a = ":;/%$#@*[](){}^"
b = input("enter the string")
y = ""
for i in b:
    if i not in a:
        y = y+i
print(y)
"""