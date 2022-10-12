def fib(n):
    f=0
    s=1
    while(f<=1000):
        if(n is f):
            return 1
        t=f+s
        f=s
        s=t
n=int(input())
if(fib(n)==1):
    print("True")
else:
    print("False")