def fun(n):
    m = str(n)
    l = m[::-1]
    m = n + int(l)
    if str(m) == str(m)[::-1]:
        return m
    else:
        return fun(m)
input_number = int(input())
x = fun(input_number)
print(x)
