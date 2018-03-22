n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    list1 = list(str1)
    list2 = list(str2)
    for l in range(len(str1)):
        if  str1[l] in str2:
            a = str1[l]
            list1.remove(a)
    for k in range(len(str2)):
        if  str2[k] in str1:
            b = str2[k]
            list2.remove(b)
    print((len(list1)+len(list2)))
