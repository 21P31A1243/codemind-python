n=int(input())
for i in range(1,n+1):
    for j in range(n-(i)):
        print(" ",end="")
    for j in range(i):
        print(i,end="")
    for j in range(i-2,-1,-1):
        print(i,end="")
    print("")