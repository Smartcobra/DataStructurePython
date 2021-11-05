def LongestIncreasingSubSequence(arr):
    n = len(arr)
    dp = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:   # or we can write dp[i] < dp[j]+1
                dp[i] = dp[j] + 1

    return max(dp)


# end of lis function


# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", LongestIncreasingSubSequence(arr))
