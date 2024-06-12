a = int(input("enter sub1 marks "))
b = int(input("enter sub2 marks "))
c = int(input("enter sub3 marks "))
avg = (a+b+c)/3
if avg >= 80:
    print("grade A")
elif (avg >= 70) and (avg <= 80):
    print("first class")
elif (avg >= 60) and (avg <= 70):
    print("second class")
elif (avg >= 50) and (avg <= 60):
    print("third class")
elif (avg >= 40) and (avg < 50):
    print("pass")
else:
    print("fail")