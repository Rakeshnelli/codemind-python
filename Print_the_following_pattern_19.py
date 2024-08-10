def print_pattern(N):
    for i in range(1, N + 1):
        print(' ' * (N - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()
N = int(input())
print_pattern(N)
