def hcf(a,b):
    small = 0
    ans = 0
    if(a>b):
        samll = a
    else:
        small = b
    for i in range(1,small+1):
        if (a%i == 0) and (b%i == 0):
            ans = i
            return ans
a = int(input("enter the value: "))
b = int(input("enter the value: "))
print("the gcd is ",hcf(a,b))   