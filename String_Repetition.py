def count_a_in_infinite_string(s, n):
    count_a_in_s = s.count('a')
    len_s = len(s)
    full_repeats = n // len_s
    remaining_chars = n % len_s
    count_a_in_remaining = s[:remaining_chars].count('a')
    total_count_a = (full_repeats * count_a_in_s) + count_a_in_remaining
    return total_count_a
s = input().strip()
n = int(input().strip())
print(count_a_in_infinite_string(s, n))
