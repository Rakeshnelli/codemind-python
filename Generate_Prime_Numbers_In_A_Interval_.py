n=int(input())
m=int(input())
c=[]
for i in range(n,m+1):
    f=0
    for j in range(1,m):
        if i%j==0:
            f+=1
    if f==2:
        c.append(i)
for k in c:
    print(k)