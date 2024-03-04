n,m=map(int,input().split())
o,e=0,0
for i in range(n,m+1):
    if i&1==0:
        o+=1
    else:
        e+=1
print(o,e)
    