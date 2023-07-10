n=input().split()
n=sorted(n)
n.sort(key=len)
print(*n)