left=int(input())
right=int(input())
def ad(n):
    for d in str(n):
        if d=='0' or n%int(d)!=0:
            return False
    return True
li=[]
for i in range(left,right+1):
    if ad(i):
        li.append(i)
for i in li:
    print(i,end=" ")

            
            