n1=int(input())
n2=int(input())
a=[]
b=[]
for i in range(1,(n1//2)+1):
    if n1%i==0:
        a.append(i)
for i in range(1,(n2//2)+1):
    if n2%i==0:
        b.append(i)
if sum(a)==n2 and sum(b)==n1:
    print("Amicable")
else:
        print("Not Amicable")