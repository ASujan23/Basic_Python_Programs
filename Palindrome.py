# Using Strings
a = input("enter the string ")
i,j= 0,len(a)-1
b = a.upper()
check = True
while i<j :
    if(b[i] != b[j]):
        check = False
        break
    i = i+1
    j = j-1
if check:
    print("palindrome")
else:
    print("not a palindrome")

# by using slice operator
"""
a = input("enter the string ")
b = a.upper()
x = b[::-1]
if x == b:
    print("palindrome")
else:
    print("not a palindrome")
"""
