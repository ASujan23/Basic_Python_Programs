n = int(input("enter the size :"))
stack = []
def push(stack,top):
    if top >= n:
        print("stack is full")
    else:
        x = int(input("enter the number "))
        stack.append(x)
        print("the added element is ",stack[-1])

def pop(stack,n):
    if top <= 0:
        print("stack is empty")
    else:
        print("the last element is deleted ",stack.pop())
        
def display(stack,top):
    if top <= 0:
        print("the list is empyt")
    else:
        print("the stack is ",stack)
while True:
    print("1-push 2-pop 3-display")
    ch = int(input("enter the choice "))
    top = len(stack)
    if ch == 1:
        push(stack,top)
    elif ch == 2:
        pop(stack,top)
    elif ch == 3:
        display(stack,top)
    else:
        print("invalid operation")
        break