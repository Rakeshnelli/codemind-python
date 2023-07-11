n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if len(str(i))>1:
        i=str(i)
        i=list(i)
        x=0
        for j in i:
            j=int(j)
            x+=j
        c.append(x)
    else:
        c.append(i)
print(sum(c))
        