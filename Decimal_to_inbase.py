def find_max_consecutive_zeros(innum, inbase):
    base_representation = ""
    number = int(innum)
    base = int(inbase)
    while number > 0:
        remainder = number % base
        base_representation = str(remainder) + base_representation
        number = number // base
    max_zeros = -1
    current_zeros = 0
    has_zero = False
    for digit in base_representation:
        if digit == '0':
            current_zeros += 1
            has_zero = True
        else:
            if current_zeros > max_zeros:
                max_zeros = current_zeros
            current_zeros = 0
    if current_zeros > max_zeros:
        max_zeros = current_zeros
    if has_zero:
        return max_zeros
    else:
        return -1
innum = input().strip()
inbase = input().strip()
print(find_max_consecutive_zeros(innum, inbase))
