def subset_sum(A, S):
    n = len(A)
    memo = [[False] * (S + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        memo[i][0] = True

    # Riempimento tabella
    for i in range(1, n + 1):
        for s in range(1, S + 1):
            if s >= A[i - 1]:
                memo[i][s] = memo[i - 1][s] or memo[i - 1][s - A[i - 1]]
            else:
                memo[i][s] = memo[i - 1][s]

    return memo[n][S]
