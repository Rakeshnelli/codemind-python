from itertools import combinations
def print_increasing_numbers(n):
    if n == 1:
        for i in range(10):
            print(i, end=" ")
        print()
        return
    digits = list(range(1, 10))
    for comb in combinations(digits, n):
        number = ''.join(map(str, comb))
        print(number, end=" ")
    print()
N = int(input())  
print_increasing_numbers(N)
