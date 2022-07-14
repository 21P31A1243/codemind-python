n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        if i!=j:
            if a[i]==a[j] and a[i]!=-1:
                a[i]=-1
                a[j]=-1
c=0
for i in a:
    if i!=-1:
        print(i,end=" ")
        c+=1
if c==0:
    print(-1)
        