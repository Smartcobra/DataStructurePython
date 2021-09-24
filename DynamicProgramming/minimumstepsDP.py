def getMinSteps(n):
    var = 2
    dp = [0] * (n + 1)
    dp[1] = 0
    for var in range(2, n + 1):
        minvalue = dp[var - 1]
        if var % 2 == 0:
            minvalue = min(minvalue, dp[var // 2])
        if var % 3 == 0:
            minvalue = min(minvalue, dp[var // 3])
        dp[var] = minvalue + 1
    return dp[n]


# driver
n = 14
print(getMinSteps(n))
