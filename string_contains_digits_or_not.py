x=int(input())
c=0
for i in range(x):
    z=input()
    for j in range(len(z)):
        if z[j] in '1 2 3 4 5 6 7 8 9 0':
            print("Yes")
            break
    else:
        print("No")