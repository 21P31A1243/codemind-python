n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+(i-1)),end=" ")
    print("")