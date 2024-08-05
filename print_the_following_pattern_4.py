def generate_pattern(N):
    pattern = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j or i + j == N - 1:
                row.append('x')
            else:
                row.append('0')
        pattern.append("".join(row))
    for line in pattern:
        print(line)
N = int(input().strip())
generate_pattern(N)