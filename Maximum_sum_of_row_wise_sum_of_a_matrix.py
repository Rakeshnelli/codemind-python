n,m=map(int,input().split())
o=[]
for i in range(n):
    l=list(map(int,input().split()))
    l=sum(l)
    o.append(l)
print(max(o))