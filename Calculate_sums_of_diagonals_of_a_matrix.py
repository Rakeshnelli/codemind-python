n=int(input())
l=[]
s=0
for i in range(n):
    m=list(map(int,input().split()))
    l.append(m)
for j in range(n):
    for k in range(n):
        if j==k or j+k==n-1:
            s+=l[j][k]
print(s)