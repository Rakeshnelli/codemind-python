n=input().split()
c=[]
for i in n:
    M=max(i)
    m=min(i)
    c.append(m)
    c.append(M)
print(*c)