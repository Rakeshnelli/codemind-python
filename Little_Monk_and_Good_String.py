n=input().lower()
v='aeiou'
c=0
m=[]
for i in n:
    if i  in v:
        c+=1
        m.append(c)
    else:
        c=0
print(max(m))