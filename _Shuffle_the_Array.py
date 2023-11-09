n=int(input())
l=list(map(int,input().split()))
x=n//2
for i in range(x):
    print(l[i],end=" ")
    print(l[i+x],end=" ")