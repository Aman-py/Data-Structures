def cal(n):
    i = n//6
    j = n//3

    if i%2 == 0 and j%2==0:
        if n%3 == 2:
            print(n+9,'MS')
        if n%3 == 1:
            print(n+11,'WS')

    if i%2== 0 and j%2!=0:
        if n%3 == 1:
            print(n+5,'AS')
        if n%3 == 2:
            print(n+3,'MS')
        
    if i%2!=0 and j%2!=0:
        if n%3 == 2:
            print(n-9,'MS')
        if n%3 == 1:
            print(n-5,'WS')

    if i%2!=0 and j%2==0:
        if n%3 == 1:
            print(n-1,'WS')
        if n%3 == 2:
            print(n-9,'MS')

    if i%2 == 0:
        if j%2 == 0 and n%3==0:
            print(n-11,'WS')
        if j%2 != 0 and n%3==0:
            print(n+7,'AS')

    if i%2 != 0:
        if j%2 != 0 and n%3==0:
            print(n-5,'AS')
        if j%2 == 0 and n%3==0:
            print(n+1,'WS')
m = int(input())

j = []

for i in range(m):
    temp = int(input())
    j.append(temp)
for k in j:
    cal(k)
