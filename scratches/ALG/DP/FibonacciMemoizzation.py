from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



def fiboMem(n, dp = {}):
    if n in dp:
        return dp[n]

    if n == 1 or n == 0:
        dp[n] = 1
        return dp[n]
    else:
        dp[n] = fiboMem(n-1) + fiboMem(n-2)
        return dp[n]


print(fiboMem(5))




