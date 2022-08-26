n=int(input())
sq=n*n
flag=0
sum,mul=0,1
while sq>0:
    rem=sq%10
    sum=sum+(rem*mul)
    mul*=10
    sq//=10
    if n==sum:
        flag=1
        break
    
if flag==1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
        