def coinChange(coins, V):
    n = len(coins)

    memo = [[float('inf') for i in range(V+1)] for j in range(n+1)]

    for i in range(n+1):
        memo[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, V+1):
            coin = coins[i-1]
            memo[i][j] = memo[i-1][j]
            if j >= coin:
                memo[i][j] = min(memo[i-1][j], 1+ memo[i][j-coin])

    return memo[n][V] if memo[n][V] != float('inf') else -1


print(coinChange([1, 2], 12))
