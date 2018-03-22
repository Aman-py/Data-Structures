n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    j = 0
    for i in range(len(str1)):
        if str1[i] not in str2:
            j+=1
    for k in range(len(str2)):
        if str2[k] not in str1:
            j+=1
    print(j)
