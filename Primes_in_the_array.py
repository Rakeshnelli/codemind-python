n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    f=0
    for j in range(1,max(l)+1):
        if i%j==0:
            f+=1
    if f==2:
        c.append(i)
print(len(c))