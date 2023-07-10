n=input().split()
s=""
for i in n:
    s+=i
mi=0
ma=0
for i in s:
    if i==min(s):
        mi+=1
    if i==max(s):
        ma+=1
print(min(s),mi,max(s),ma)