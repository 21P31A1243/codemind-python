n=int(input())
s=0
p=1
while n>0:
    r=n%10
    s=s+r
    p=p*r
    n=n//10
digit=p-s
print(digit)