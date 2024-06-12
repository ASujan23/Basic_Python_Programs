st1 = input("enter the string:")
st2 = ""
for i in range(len(st1)):
    if(i % 2 == 0):
        st2 = st2 + st1[i]
print(st2)