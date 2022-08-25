n=int(input())
sum,mul=0,1
while(n!=0):
    sum+=n%10
    mul*=n%10
    n//=10
if(sum==mul):
    print("Spy Number")
else:
    print("Not Spy Number")