a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=0
B=0
X=0
for i in range(len(a)):
    if a[i]>b[i]:
        A+=1
    elif a[i]<b[i]:
        B+=1
    else:
        X=1
print(A,B)