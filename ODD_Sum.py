n=int(input())
arr=list(map(int,input().split()))
o=e=0
for i in range(n):
    if(arr[i]%2==1):
        e+=arr[i]
print(e)