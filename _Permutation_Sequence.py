import math

def getPermutation(n, k):
    numbers = [str(i) for i in range(1, n + 1)]
    result = ""

    k -= 1  
    while n > 0:
        n -= 1
        index = k // math.factorial(n)
        k = k % math.factorial(n)
        result += numbers.pop(index)

    return result

n,k=map(int,input().split())
print(getPermutation(n, k))  