def can_win(N, A, B, K):
    divisible_by_A = N // A
    divisible_by_B = N // B
    divisible_by_both = N // (A * B)

    problems_solved = divisible_by_A + divisible_by_B - 2 * divisible_by_both

    if problems_solved >= K:
        return "Win"
    else:
        return "Lose"
T = int(input())
for _ in range(T):
    N, A, B, K = map(int, input().split())
    result = can_win(N, A, B, K)
    print(result)
