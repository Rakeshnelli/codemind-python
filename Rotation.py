t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    k=len(l)-m
    o=l[k:]+l[:k]
    print(*o)