def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    primes = [num for num in range(limit + 1) if sieve[num]]
    return primes
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if abs(arr[left] - target) < abs(arr[right] - target):
        return arr[left]
    else:
        return arr[right]
primes = sieve_of_eratosthenes(2000100)
n = int(input())
for i in range(n):
    input_number = int(input())
    result = binary_search(primes, input_number)
    print(result)
