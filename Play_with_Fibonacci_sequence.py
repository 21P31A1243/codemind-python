n=int(input())
f=0
s=1
t=f+s
while(n>0):
    print(f,end=" ")
    f=s
    s=t
    t=f+s
    n-=1
