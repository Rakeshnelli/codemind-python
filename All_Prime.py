def is_prime_digit(digit):
    prime_digits = {'2', '3', '5', '7'}
    return digit in prime_digits
def check_prime_digits(n):
    digits = str(n)
    for digit in digits:
        if not is_prime_digit(digit):
            return "False"
    
    return "True"
n = int(input())
print(check_prime_digits(n))
