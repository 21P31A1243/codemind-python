n=int(input())
a=str(n)
if '6' in a:
    l=list(a)
    i=l.index('6')
    l[i]='9'
    fi="".join(l)
    print(int(fi))
else:
    print(n)