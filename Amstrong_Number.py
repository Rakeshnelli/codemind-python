def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += int(digit) ** num_digits
    return sum_of_powers == n
n = int(input())
if is_armstrong_number(n):
    print("YES")
else:
    print("NO")
