n=int(input())
arr=list(map(int,input().split()))
k=int(input())
hi=0
for i in arr:
    if hi<i:
        hi=i
for i in arr:
    if i+k>=hi:
        print("True",end=" ")
    else:
        print("False",end=" ")
    