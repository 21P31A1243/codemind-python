n=int(input())
arr=list(map(int,input().split()))
arr2=[]
for i in range(n):
    c=0
    for j in range(n):
        if i!=j:
            if arr[i]>arr[j]:
                c+=1
    arr2.append(c)
for i in range(n):
    print(arr2[i],end=" ")
        