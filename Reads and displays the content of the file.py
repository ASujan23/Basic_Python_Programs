f = open("abc.txt","w")
f.write("i am a student\n")
f.write("studing in S & S college\n")
f.write("which is located in tekkali\n")
f.close()
f2 = open("sai.txt","r")
print(f2.read())