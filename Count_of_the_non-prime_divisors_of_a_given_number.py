n=int(input())
c=[]
x=[]
for i in range(1,n+1):
    if n%i==0:
        c.append(i)
for j in c:
    f=0
    for k in range(1,n+1):
        if j%k==0:
            f+=1
    if f!=2:
        x.append(j)
print(len(x))