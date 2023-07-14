n=input().lower()
l=list(n)
c=""
for i in l:
    if (i not in c) and i.isalnum()==True:
        c+=i
x=sorted(c)
u=''.join(x)
print(u)
