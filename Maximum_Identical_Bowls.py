n=int(input())
l=list(map(int,input().split()))
m=sum(l)
while n:
    if m%n==0:
        print(n)
        break
    n=n-1
