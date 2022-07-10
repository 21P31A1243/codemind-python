a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    sum1=0
    for j in range(i,b+1):
        sum1+=j
        if sum1%2!=0:
            count+=1
    
print(count)
        
        
        