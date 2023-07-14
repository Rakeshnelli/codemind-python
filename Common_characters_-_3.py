n=input().lower()
m=list(set(list(n)))
n=n.split()
c=[]
for i in m:
    d=0
    for j in n:
        if i in j and i.isalnum():
            d+=1
    if d==len(n):
        c.append(i)
if c:
    print(min(c))
else:
    print(-1)