n=int(input())
x=str(n)
l=x[::-1]
l=int(l)
f=0
F=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
for j in range(1,l+1):
    if l%j==0:
        F+=1
if f==2 and F==2:
    print('circular prime')
elif f==2:
    print('prime but not a circular prime')
else:
    print('not prime')