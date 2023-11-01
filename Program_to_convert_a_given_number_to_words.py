def numberToWords(n):
    under_20 = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    thousands = ["", "thousand", "million", "billion"]

    if n == 0:
        return under_20[0]

    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return under_20[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + helper(num % 10)
        else:
            return under_20[num // 100] + " hundred " + helper(num % 100)

    result = ""
    i = 0
    while n > 0:
        if n % 1000 != 0:
            result = helper(n % 1000) + thousands[i] + " " + result
        n //= 1000
        i += 1

    return result.strip()

number = int(input())

words = numberToWords(number)
print(words)
