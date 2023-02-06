def perfectsquares(n):
    if n == 1 or n==2 or n==3:
        return 1
    res = n
    for x in range(1, n + 1):
        temp = x * x
        if temp > n:
            break
        else:
            res = min(res, 1+ perfectsquares (n- temp))
    return res
print(perfectsquares(12))
print(perfectsquares(13))
print(perfectsquares(1))
print(perfectsquares(4))
print(perfectsquares(3))
