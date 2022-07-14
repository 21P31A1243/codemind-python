n=int(input())
arr=list(map(int,input().split()))
k=0
for i in arr:
    c=0
    while i>0:
        i//=10
        c+=1
    if c%2==0:
        k+=1
        
print(k)
    