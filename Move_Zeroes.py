n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(n):
    if a[i]!=0:
        b.append(a[i])
    else:
        c+=1
for i in range(c):
    b.append(0)
for i in range(len(b)):
    print(b[i],end=" ")
        
        