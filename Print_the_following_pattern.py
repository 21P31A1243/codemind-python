a=int(input())
li = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(a):
    for j in range(a-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print(li[j],end="")
    for j in range(i-1,-1,-1):
        print(li[j],end="")
    print("")