n = int(input("enter a number:"))
order = len(str(n))
sum =0
temp = n
while n>0:
    ld = n%10
    fact = 1
    for i in range(1,ld+1):
        fact *= i
    sum += fact
    n //= 10
if temp == sum:
    print("strong number")
else:
    print("not an strong number")