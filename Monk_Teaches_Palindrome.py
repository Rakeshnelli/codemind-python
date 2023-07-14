n=int(input())
for i in range(n):
    m=input()
    x=m[::-1]
    if m==x and len(m)%2==0:
        print("YES","EVEN")
    elif m==x and len(m)%2!=0:
        print("YES","ODD")
    else:
        print("NO")