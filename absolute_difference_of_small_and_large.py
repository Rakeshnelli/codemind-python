n=input().split()
c=[]
for i in n:
    M=max(i)
    m=min(i)
    c.append(ord(M)-ord(m))
print(*c)