def checkSubsetSum(arr, sum):
    if len(arr) == 0:
        return False
    if sum == 0:
        return True
    n = len(arr)
    rows, cols = (n + 1, sum + 1)
    # dp = [[0] * cols] * rows
    dp = [[False for i in range(cols)] for i in range(rows)]

    for i in range(rows):
        dp[i][0] = True

    for i in range(1, cols):
        dp[0][i] = False

    for i in range(1, rows):
        for j in range(1, cols):
            if j >= arr[i - 1]:  ## including the the current sum
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])
            # if j < arr[i - 1]:
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    return dp[n][sum]


### Invoking
arr = [1, 5, 3, 7, 4]
sum = 100
print(checkSubsetSum(arr, sum))
