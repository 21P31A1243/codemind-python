n=int(input())
t=n
for i in range(n):
    for j in range(n):
        if i==j:
            print(t,end=" ")
        elif i+j==n-1:
            print(t,end=" ")
        else:
            print("",end=" ")
    t-=1
    print("")
    