def getsMinStepsHelper(n, memo):
    if n == 1:
        return 0
    if memo[n] != -1:
        return memo[n]
    res = getsMinStepsHelper(n - 1, memo)
    if n % 2 == 0:
        res = min(res, getsMinStepsHelper(n // 2, memo))
    if n % 3 == 0:
        res = min(res, getsMinStepsHelper(n // 3, memo))

    memo[n] = res + 1
    return memo[n]


def getsMinSteps(n):
    memo = list(range(n + 1))
    for i in range(n + 1):
        memo[i] = -1
    return getsMinStepsHelper(n, memo)


# driver program
n = 10
print(getsMinSteps(n))
