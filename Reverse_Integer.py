n=int(input())
if n<0:
    n=-n
    n=str(n)
    n=list(n)
    n.reverse()
    x=''.join(n)
    x=int(x)
    print(-x)
else:
    n=str(n)
    n=list(n)
    n.reverse()
    x=''.join(n)
    x=int(x)
    print(x)
    
    