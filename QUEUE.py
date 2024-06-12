n = int(input("enter the size:"))
queue = []
def push(queue,top):
    if top >= n:
        print("queue is full")
    else:
        x = int(input("enter the number "))
        queue.append(x)
        print("the added element is ",queue[-1])

def pop(queue,n):
    if top <= 0:
        print("queue is empty")
    else:
        print("the first element is deleted ",queue.pop(0))

def display(queue,top):
    if top <= 0:
        print("the list is empyt")
    else:
        print("the queue is ",queue)
while True:
    print("1-push 2-pop 3-display")
    ch = int(input("enter the choice "))
    top = len(queue)
    if ch == 1:
        push(queue,top)
    elif ch == 2:
        pop(queue,top)
    elif ch == 3:
        display(queue,top)
    else:
        print("invalid operation")
        break