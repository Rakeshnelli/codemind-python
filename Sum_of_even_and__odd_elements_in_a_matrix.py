r,c=map(int,input().split())
C=[]
e=0
o=0
for i in range(r):
    l=list(map(int,input().split()))
    C.append(l)
for j in range(r):
    for k in range(c):
        if C[j][k]%2==0:
            e+=C[j][k]
        else:
            o+=C[j][k]
print(e,o)