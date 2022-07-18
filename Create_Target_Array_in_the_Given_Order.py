n1=int(input())
a1=list(map(int,input().split()))
n2=int(input())
a2=list(map(int,input().split()))
res=[]
for i in range(n1):
    res.insert(a2[i],a1[i])
for i in range(n2):
    print(res[i],end=" ")