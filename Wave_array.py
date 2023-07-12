n=int(input())
a=list(map(int,input().split()))
c=0
b=0
for i in range(1,n-1,2):
    if a[i-1]<a[i] and a[i]>a[i+1] or a[i-1]>a[i] and a[i]<a[i+1]:
        c+=1
    else:
        b+=1
if c==0 or b!=0:
    print('no')
else:
    print('yes')