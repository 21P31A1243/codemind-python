n=int(input())
a=0
if n<0:
    n=-(n)
    a=1
else:
    n=n
sum,mul=0,1
while(n>0):
    rem=n%10
    sum=(sum*10)+rem
    n//=10
if a==1:
    print(-(sum))
else:
    print(sum)
    
