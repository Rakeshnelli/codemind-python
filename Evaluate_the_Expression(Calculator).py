def calculate(s):
    stack = []
    result, number, sign = 0, 0, 1

    for i in range(len(s)):
        if s[i].isdigit():
            number = number * 10 + int(s[i])

        elif s[i] == '+':
            result += sign * number
            number = 0
            sign = 1

        elif s[i] == '-':
            result += sign * number
            number = 0
            sign = -1

        elif s[i] == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1

        elif s[i] == ')':
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()

    result += sign * number
    return result

s1 = input()
print(calculate(s1))  

