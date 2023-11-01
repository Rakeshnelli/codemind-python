def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def product_of_primes_and_non_primes(arr):
    product_non_primes = 1
    product_primes = 1

    for num in arr:
        if is_prime(num):
            product_primes *= num
        else:
            product_non_primes *= num

    return abs(product_non_primes - product_primes)
N = int(input())
array = list(map(int, input().split()))
result = product_of_primes_and_non_primes(array)
print(result)
