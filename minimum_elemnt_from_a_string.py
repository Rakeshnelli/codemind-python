def find_minimum_element(word):
    min_char = min(word)
    lower_case_min = min(word.lower())
    if min_char.isupper() and lower_case_min in word:
        return lower_case_min
    return min_char
input_string = input().strip()
words = input_string.split()
last_word = words[-1]
result = find_minimum_element(last_word)
print(result)
