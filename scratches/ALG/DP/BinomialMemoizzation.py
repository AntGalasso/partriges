def iterativeBinomial(n, r, memo = {}):
    for i in range(n+1):
        memo[(i, 0)] = 1
    for i in range(r+1):
        memo[(i, i)] = 1
    for j in range(n+1):
        for i in range(j, r+1):
            memo[(n, r)] = memo[(i-1, j)] + memo[(i-1, j-1)]

    return memo[(n, r)]


def binomial(n, r, memo={}):
    if (n, r) in memo:
        return memo[(n, r)]
    if r == 0 or n == r:
        memo[(n, r)] = 1
    else:
        memo[(n, r)] = binomial(n-1, r-1) + binomial(n-1, r)

    return memo[(n, r)]


print(binomial(5, 4))
print(iterativeBinomial(5, 3))

