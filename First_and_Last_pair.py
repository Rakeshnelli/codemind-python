n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
d=1
q=n//2
if n%2!=0:
    for c in range(q):
        a.append(l[c])
        a.append(l[n-d])
        c+=1
        d+=1
    a.append(l[q])
    print(*a,end=" 0")
else:
    for c in range(q):
        a.append(l[c])
        a.append(l[n-d])
        c+=1
        d+=1
    print(*a)