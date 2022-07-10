arr=list(map(int,input().split(",")))
l1 = []
c = 0
for i in arr:
    sum1 = 0
    for j in range(1,i+1):
        if i%j==0:
            sum1+=j
    if sum1 in arr:
        l1.append(i)
        c+=1
if c==0:
    print("-1")
else:
    l1.sort()
    for i in l1:
        print(i,end = " ")
    

        
