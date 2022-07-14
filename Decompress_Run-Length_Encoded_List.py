n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n,2):
    a=arr[i]
    b=arr[i+1]
    for j in range(a):
        print(b,end=" ")
