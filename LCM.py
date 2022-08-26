a,b=[int(i) for i in input().split()] 
if a>b:
    high=a
else:
    high=b
value=high
while True:
    if high%a==0 and high%b==0:
        print(high)
        break
    else:
        high+=value