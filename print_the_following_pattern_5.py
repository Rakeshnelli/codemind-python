def generate_pattern(N):
    pattern = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append('0')
            else:
                row.append('x')
        pattern.append("".join(row))
    for line in pattern:
        print(line)
N = int(input().strip())
generate_pattern(N)