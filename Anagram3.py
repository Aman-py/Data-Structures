n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    list3 = list(str1)+list(str2)
    j = 0
    for l in range(len(list3)):
        if (list3[l] in str1) and (list3[l] in str2):
            j+=1
        
    print(len(list3))
