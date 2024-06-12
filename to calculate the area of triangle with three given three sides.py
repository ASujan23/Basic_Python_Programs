a = int(input("enter a number "))
b = int(input("enter b number "))
c = int(input("enter c number "))
s = (a+b+c)/2
ans = s*(s-a)*(s-b)*(s-c)
ans = ans**0.5
print("the area of traingle is ",ans)