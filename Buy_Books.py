n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
s1=0
s2=0
for i in arr1:
    s1+=i
for i in arr2:
    s2+=i
if s1>s2:
    print(0)
else:
    print(s2-s1)