"""
Наибольший общий делитель рекурсией
"""


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(25478, 178346))
