s=input()
n=int(input())
count=c=sl=0
sl=len(s)
for i in s:
    if i=='a':
        c+=1
b=n//sl
r=n%sl
count=c*b
for i in range(r):
    if s[i]=='a':
        count+=1
print(count)