import re
n=input("Enter a String")
res=re.findall("[A-Z]",n)
res1=re.split("[a-z]",n)
res2=re.sub("[0-9]","",n)
res3=re.search("\s",n)
res4=re.subn("[a-d]",'z',n)
res5=re.match("^a",n)
print(res)
print(res1)
print(res2)
print(res4)
if (res3):
    print("Found")
else:
    print("Not Found")
if (res5):
    print("Found")
else:
    print("Not Found")