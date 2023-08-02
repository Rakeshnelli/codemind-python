n=int(input())
k=e=0
if n<=1:
    print("Not Mega Prime")
else:
    for i in range(2,n):
        if n%i==0:
            e=1
            break
    if e==1:
        print("Not Mega Prime")
    else:
        while n:
            k=n%10
            j=0
            if k==1:
                j=1
                break
            else:
                for i in range(2,k):
                    if k%i==0:
                        j=1
                        break
            n=n//10
        if j==0:
            print("Mega Prime")
        else:
            print("Not Mega Prime")