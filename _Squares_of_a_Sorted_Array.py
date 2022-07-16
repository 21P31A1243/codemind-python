n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(a[i]*a[i])
b.sort()
for i in b:
    print(i,end=" ")