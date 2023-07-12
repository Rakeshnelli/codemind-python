n=int(input())
c=[]
for i in range(1,n):
    f=0
    for j in range(1,n):
        if i%j==0:
            f+=1
    if f==2:
        c.append(i)
o=[]
for k in c:
    for l in range(len(c)):
        if k*c[l]==n:
            o.append(k)
            o.append(c[l])
if len(o)>0:
    print(o[0],o[1])
else:
    print(-1)
