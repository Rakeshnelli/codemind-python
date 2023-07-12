n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    for j in range(0,len(l)-1):
        if sum(l[:j+1])==sum(l[j+2:]):
            print(j+1)
            break
    else:
        print(-1)
