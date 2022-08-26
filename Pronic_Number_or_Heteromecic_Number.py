n=int(input())
flag=0
if n%2==0:
    for i in range(n):
            if (i*(i+1)==n):
                flag=1
                break
    if flag==1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

    
