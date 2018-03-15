def creatarray():
    arr = [int(temp) for temp in input().strip().split(' ')]
    return arr

def adjlist(arr,next):
    for i in arr:
        y = i
        while True:
            x = int(input())
            if x in arr:
                y.next = x
                y = x
            elif x == None:
                break

arr = creatarray()
adjlist(arr)
