t=int(input())
v=0
for i in range(t):
    op=input()
    if(op=="++X"):
        v+=1
    if(op=="X++"):
        v+=1
    if(op=="--X"):
        v-=1
    if(op=="X--"):
        v-=1
print(v)
    

