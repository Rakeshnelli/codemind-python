n, m = map(int, input().split())
o = []

# Taking input
for i in range(n):
    l = list(map(int, input().split()))
    o.append(l)

# Finding the column-wise sum
column_sums = []
for j in range(m):
    column_sum = 0
    for i in range(n):
        column_sum += o[i][j]
    column_sums.append(column_sum)
print(*column_sums)
