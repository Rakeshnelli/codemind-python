n= int(input())
m= int(input())
prime_numbers = []
for num in range(n,m+1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
print(len(prime_numbers))
