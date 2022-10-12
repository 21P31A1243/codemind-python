def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if(isPrime(i)):
        print(i)