def lcs(x, y):
    m = len(x)
    n = len(y)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    #riempo la tabella secondo la recurrence

    #recurrence: OPT(i, j) = {
    #       0 per i = 0 e j = 0
    #       1 + dp[i-1][j-1] se x[i] == y[j]
    #       max{dp[i-1][j], dp[i][j-1]}
    # }

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


print(lcs('ant', 'ami'))


