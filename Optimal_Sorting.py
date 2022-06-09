t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c=0
    num=0
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]>a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                c+=1
    if c==0:
        print(0)
    else:
        num = a[n-1]-a[0]
        print(num)
        