n=input().lower()
n=sorted(n)
l=list(n)
c=[]
for i in l:
    if l.count(i)==1 and i.isalnum()==True:
        c.append(i)
c=''.join(c)
print(c)
