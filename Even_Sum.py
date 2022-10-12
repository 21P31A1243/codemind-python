n=int(input())
arr=list(map(int,input().split()))
e=0
for i in range(n):
    if(arr[i]%2==0):
        e+=arr[i]
print(e)