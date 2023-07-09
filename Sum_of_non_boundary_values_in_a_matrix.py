n,m=map(int,input().split())
o=[]
for i in range(n):
    l=list(map(int, input().split()))
    o.append(l)
p=0
for i in range(1,n-1):
    for j in range(1,m-1):
            p+=o[i][j]
print(p)
