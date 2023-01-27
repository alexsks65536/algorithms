"""
Возвращает минимальное число
"""
# def gcd(m, n):
#     while m != n:
#         if m > n:
#             m -= n
#         else:
#             n -= m
#     return m


"""
Возвращает наибольший общий делитель
"""


def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


"""
RecursionError: maximum recursion depth exceeded
"""


# def gcd(m, n):
#     return (m / gcd(m, n)) * n


"""
Возвращает наибольший общий делитель
"""


# def gcd(m, n):
#     while n != 0:
#         m, n = n, m % n
#     return m


print(gcd(3219, 18))
