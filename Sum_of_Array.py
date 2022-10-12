n=int(input())
arr=list(map(int,input().split()))
e=0
for i in range(n):
    e+=arr[i]
print(e)