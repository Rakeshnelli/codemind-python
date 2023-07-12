n=input()
c=1
for i in range(1,len(n)-1):
    if 65<=ord(n[i])<=95:
        c+=1
print(c)