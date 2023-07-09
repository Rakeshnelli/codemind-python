n, m = map(int, input().split())
o = []
for i in range(n):
    l = list(map(int, input().split()))
    o.append(l)
column_sums = []
for j in range(m):
    column_sum = 0
    for i in range(n):
        column_sum += o[i][j]
    column_sums.append(column_sum)
print(max(column_sums))
