t=int(input())
flag=0
for i in range(t):
    n=int(input())
    for i in range(n):
        if(i*i==n):
            flag=1
            break
        else:
            flag=0
    if (flag==1):
        print("True")
    else:
        print("False")
