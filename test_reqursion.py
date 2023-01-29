def akk(m, n):
    if m > 0 and n == 0:
        return akk(m - 1, 1)
    if m == 0:
        return n + 1
    if m > 0 and n > 0:
        return akk(m - 1, akk(m, n - 1))


print(akk(0, 2))
