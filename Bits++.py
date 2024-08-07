def final_value_of_x(n, statements):
    x = 0
    for statement in statements:
        if '++' in statement:
            x += 1
        elif '--' in statement:
            x -= 1
    return x
n = int(input())
statements = [input().strip() for _ in range(n)]
print(final_value_of_x(n, statements))
