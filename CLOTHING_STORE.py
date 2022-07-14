
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n):
        if i!=j:
            if a[i]==a[j] and a[i]!=-1:
                a[i]=-1
                a[j]=-1
                c+=1
print(c)

        