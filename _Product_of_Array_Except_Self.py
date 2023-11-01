n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    f=1
    for j in range(len(l)):
        if i!=j:
            f=f*l[j]
    print(f,end=" ")