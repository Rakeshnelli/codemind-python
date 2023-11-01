def replaceElements(arr):
    n = len(arr)
    max_from_right = arr[n - 1]
    arr[n - 1] = -1

    for i in range(n - 2, -1, -1):
        temp = arr[i]
        arr[i] = max_from_right
        max_from_right = max(max_from_right, temp)

    return arr

n = int(input()) 
arr = list(map(int, input().split()))  
result = replaceElements(arr)
print(*result)
