n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(2,n):
    if l[i-1]+l[i-2]==l[i]:
        c=1
    else:
        c=0
        break
if c==1:
    print("yes")
else:
    print("no")