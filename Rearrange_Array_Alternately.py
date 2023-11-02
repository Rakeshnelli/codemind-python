def rearrange_array_alternatively(arr):
    n = len(arr)
    # Maximum index
    max_idx = n - 1
    # Minimum index
    min_idx = 0
    # Store the maximum element
    max_elem = arr[max_idx] + 1

    for i in range(n):
        # Even indexed elements will have maximum elements
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            # Odd indexed elements will have minimum elements
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1

    # Restoring original array
    for i in range(n):
        arr[i] = arr[i] // max_elem

    return arr

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the array size and elements for each test case
    N = int(input())
    array = list(map(int, input().split()))

    # Rearrange the array alternatively
    result = rearrange_array_alternatively(array)
    
    # Output the modified array
    print(*result)
