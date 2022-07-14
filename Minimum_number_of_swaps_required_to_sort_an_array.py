n=int(input())
a=list(map(int,input().split()))
b=a.copy()
b.sort()
c=0
for i in range(n):
    if a[i]!=b[i]:
        ind=a.index(b[i])
        a[i],a[ind]=a[ind],a[i]
        c+=1
print(c)
    