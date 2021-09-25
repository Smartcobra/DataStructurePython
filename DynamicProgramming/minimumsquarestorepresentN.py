import sys


def getminsquare(n):
    if n == 0:
        return 0
    minAns = sys.maxsize
    for i in range(1, n + 1):
        tmp = i * i
        if tmp > n:
            break
        else:
            minAns = min(minAns, getminsquare(n - tmp))
    return 1 + minAns


# Driver
print(getminsquare(6))
