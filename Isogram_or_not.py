n=input()
n=list(n)
x=[]
c=0
for i in n:
    if i not in x:
        x.append(i)
if len(n)==len(x):
    print(True)
else:
    print(False)