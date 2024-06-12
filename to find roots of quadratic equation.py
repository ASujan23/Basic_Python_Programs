a = int(input("enter a number "))
b = int(input("enter b number "))
c = int(input("enter c number "))
dis = b*b-4*a*c
if dis:
    sq = dis**0.5
    fir,sec = (-b+sq)/2*a,(-b-sq)/2*a
    print(fir,sec)
elif dis == 0:
    fir,sec = -b/(2*a)
    print(fir,sec)
else:
    print("roots are imaginary")