n,m=map(int,input().split())
o=[]
for i in range(n):
    l=list(map(int, input().split()))
    o.append(l)
p=0
for i in range(n):
    for j in range(m):
        if i==j or i+j==n-1:
            p+=o[i][j]
print(p)
