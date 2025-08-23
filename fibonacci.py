#top down DP(memoization)
def memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memoization(n - 1, memo) + memoization(n - 2, memo)
    return memo[n]

def tabulation(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]


print(memoization(10))
print(tabulation(10))
