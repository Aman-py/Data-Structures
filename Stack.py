def setlimit():
    n = int(input())
    return n

def genstack():
    stack = []
    return stack

def isempty():
    return len(stack) == 0

def peek():
    return len(stack) == n

def push(stack):
    if peek():
        print("Overflow")
    else:
        z = input()
        stack.append(z)
        print(z,'is pushed in stack')

def pop(stack):
    if isempty():
        print("Underflow")
    else:
        z=stack.pop()
        z
        print(z,"pop from stack")

stack = genstack()
n=setlimit()
push(stack)
push(stack)
push(stack)
pop(stack)
print(stack)
