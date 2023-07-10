n=int(input())
l=list(map(int,input().split()))
c=1
d=0
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        d=1
    else:
        c=0
if d==1 and c==1:
    print('yes')
else:
    print('no')