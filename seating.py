T = int(input())
     
for i in range(1,T+1):
    N=int(input())
    if N%12==0:
        print(N-11,'WS')
    elif N%12==11:
        print(N-9,"MS")
    elif N%12==10:
        print(N-7,"AS")
    elif N%12==9:
        print(N-5,'AS')
    elif N%12==8:
        print(N-3,"MS")
    elif N%12==7:
        print(N-1, "WS")
    elif N%12==6:
        print(N+1, "WS")
    elif N%12==5:
        print(N+3, 'MS')
    elif N%12==4:
        print(N+5, "AS")
    elif N%12==3:
        print(N+7, "AS")
    elif N%12==2:
        print(N+9, "MS")
    elif N%12==1:
        print(N+11, "WS")
