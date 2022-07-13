n=int(input())
k=n
size=(2*n)-1
arr=[[0 for i in range(size)]for j in range(size)]
for i in range(n):
    for j in range(i,size-i):
        arr[j][i]=k
        arr[j][size-i-1]=k
        arr[i][j]=k
        arr[size-i-1][j]=k
    k-=1
for i in range(size):
    for j in range(size):
        print(arr[i][j],end=" ")
    print("")