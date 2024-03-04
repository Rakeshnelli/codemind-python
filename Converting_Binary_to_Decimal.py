n=int(input())
n=str(n)
l=len(n)
ans=0
for i in n:
    ans+=(int(i))*(2**l)
    l-=1
print(ans//2)
    