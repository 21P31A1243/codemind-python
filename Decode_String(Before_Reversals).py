num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    s = input()
    while b>0:
        s1 = s[:b]
        s1 = s1[::-1]
        s = s1 + s[b:]
        b-=1
    print(s)