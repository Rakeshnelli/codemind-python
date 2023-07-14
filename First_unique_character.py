n=input().lower()
l=list(n)
c=[]
for i in l:
    if l.count(i)==1 and i.isalnum()==True:
        print(i)
        break
else:
    print(-1)