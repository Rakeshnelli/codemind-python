n= int(input())
m= int(input())
prime_numbers = []
for i in range(n,m+1):
    if i > 1:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
print(len(prime_numbers))
