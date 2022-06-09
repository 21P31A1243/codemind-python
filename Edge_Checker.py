a,b = [int(x) for x in input().split()]
res = (a-b)
if res < 0:
    res = -(res)
else:
    res = res
if res==1 or res==9:
    print("Yes")
else:
    print("No")