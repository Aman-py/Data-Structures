n = int(input())

arr = list(range(2,n))
arr_A = []

for i in arr:
    j = i
    m = arr.index(i)
    arr_A.append(i)
    for k in arr[m+1:]:
        if k%i == 0:
            arr.remove(k)
str_1 = (' '.join( str(e ) for e in arr_A))
print(str_1)

