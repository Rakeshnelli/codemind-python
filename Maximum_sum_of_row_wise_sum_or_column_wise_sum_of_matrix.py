r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    l=sum(l)
    m.append(l)
print(max(m))
