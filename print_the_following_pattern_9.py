def generate_pattern(N):
    for i in range(1, N + 1):
        for _ in range(N - i):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print(i, end="")
        print()
N = int(input().strip())
generate_pattern(N)