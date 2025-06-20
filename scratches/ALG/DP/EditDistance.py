def editDistance(x, y):
    n = len(x)
    m = len(y)

    memo = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range (n+1):
        memo[i][0] = i
    for j in range (m+1):
        memo[0][j] = j



    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if x[i - 1] == y[j - 1] else 1

            memo[i][j] = min(memo[i][j-1] + 1, memo[i-1][j] + 1, memo[i-1][j-1] + cost)


    return memo[n][m]

print(editDistance('aaaaa', 'autio'))

