n=int(input())
flag=0
for p in [2,3,5]:
    while n%p==0:
        n//=p
    if n==1:
        flag=1
if flag==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
