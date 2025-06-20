def examProblem(points, times, T):
    n = len(points)
    memo = [[0 for _ in range(T + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(T + 1):
            if j < times[i - 1]:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - times[i - 1]] + points[i - 1])

    return memo[n][T]

points = [3, 7, 2, 9]
times = [2, 5, 1, 6]
T = 8

print(examProblem(points, times, T))

