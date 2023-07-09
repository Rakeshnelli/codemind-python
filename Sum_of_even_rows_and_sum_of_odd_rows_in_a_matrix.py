r,c=map(int,input().split())
m=[]
e=[]
o=[]
for i in range(r):
    l=list(map(int,input().split()))
    l=sum(l)
    m.append(l)
for j in range(len(m)):
    if j%2==0:
        e.append(m[j])
    else:
        o.append(m[j])
print(sum(e),sum(o))
