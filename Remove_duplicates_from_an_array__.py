n=int(input())
li=list(map(int,input().split()))
ne=[]
for i in range(len(li)):
    if li[i] not in ne:
        ne.append(li[i])
for i in range(len(ne)):
    print(ne[i],end=" ")