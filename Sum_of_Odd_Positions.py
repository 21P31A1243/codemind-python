n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(n):
    if(i%2==1):
        sum+=arr[i]
print(sum)
        