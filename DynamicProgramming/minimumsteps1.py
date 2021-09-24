def getminsteps(n):
    if n == 1:
        return 0
    res = getminsteps(n - 1)
    if n % 2 == 0:
        res = min(res, getminsteps(n // 2))
    if n % 3 == 0:
        res = min(res, getminsteps(n // 3))

    return res


ans = getminsteps(10)
print(ans)
