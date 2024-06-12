n = int(input("enter a number: "))
order = len(str(n))
sum =0
temp = n
while n>0:
    ld = n%10
    sum += ld**order
    n //= 10
if temp == sum:
    print("armstrong number")
else:
    print("not an armstrong number")