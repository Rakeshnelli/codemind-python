n=int(input())
c=0
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    for j in range(1,m):
        if l[j-1]>l[j]:
            c+=1
    if c==0:
        print(c)
    else:
        x=max(l)
        y=min(l)
        print(x-y)