a = input("enter the stirng: ")
char,upper,lower,digit = 0,0,0,0
for i in a:
    if (i >= "a" and i<="z"):
        lower += 1
    elif (i >= "A" and i<="Z"):
        upper += 1
    elif (i >= "0" and i<="9"):
        digit += 1
char = lower + upper + digit
print("the digits are ",digit)
print("the lower are ",lower)
print("the upper are ",upper)
print("the charecters are ",char)

# by using inbuilt functions
"""
a = input("enter the stirng ")
char,upper,lower,digit = 0,0,0,0
for i in a:
    if(i.islower()):
        lower += 1
    elif (i.isupper()):
        upper += 1
    for i in a:
        if(i.isdigit()):
            digit += 1
        elif (i.isalpha()):
            char += 1
char = lower + upper + digit
print("the digits are ",digit)
print("the lower are ",lower)
print("the upper are ",upper)
print("the charecters are ",char)
"""