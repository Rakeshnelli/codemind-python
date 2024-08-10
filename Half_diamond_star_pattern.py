# Function to print the half diamond star pattern
def print_half_diamond(n):
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)
n = int(input())
if 3 <= n <= 100:
    print_half_diamond(n)
else:
    print()
