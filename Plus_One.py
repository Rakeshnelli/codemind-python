def plusOne(digits):
    n = len(digits)
    carry = 1  
    for i in range(n - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10  
        carry = total // 10  
    if carry:
        digits.insert(0, carry)  
    return digits
N = int(input())
elements = list(map(int, input().split()))
result = plusOne(elements)
print(*result)
