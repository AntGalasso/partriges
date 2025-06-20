def iterSumToX(n, m, X):
    memo = [[0 for i in range(X+1)] for j in range(n+1)]

    memo[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, X+1):
            memo[i][j] = sum(memo[i-1][j-k] for k in range(1, m+1) if j - k >= 0)

    return memo[n][X]


print(iterSumToX(2, 6, 8))


