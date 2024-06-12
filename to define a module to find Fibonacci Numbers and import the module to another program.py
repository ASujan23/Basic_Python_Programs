#this module is save as fibochhi.py
def fib(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(n-2):
        c = a+b
        print(c)
        a = b
        b = c

#in another python file importing fibnochhi module
import fibnochhi
n = int(input("enter the n value "))
fibnochhi.fib(n)