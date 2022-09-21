def isPrime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False
n=int(input())
res=isPrime(n)
if(res==True):
    flag=1
    while(n>0):
        rem=n%10
        if(isPrime(rem)):
            flag=1
        else:
            flag=0
            break
        n//=10
    if(flag==1):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
            
            