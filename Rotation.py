t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(k):
        fi=arr[0]
        arr[0]=arr[n-1]
        for j in range(1,n):
            temp=arr[j]
            arr[j]=fi
            fi=temp
    for i in range(n):
        if i<n-1:
            print(arr[i],end=" ")
        else:
            print(arr[i])

            
        
        