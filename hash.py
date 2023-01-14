import hashlib
from uuid import uuid4
from recursion import separator


if __name__ == "__main__":

    separator("Известные хеш-функции в Python")

    separator("список все алгоритмов, доступных в системе")

    print(hashlib.algorithms_available)

    separator("существующие алгоритмы модуля")

    print(hashlib.algorithms_guaranteed)


"""Примеры с md5"""
separator("Примеры с md5")

hash_obj = hashlib.md5(b'Testing md5 func')
print(hash_obj)  # -> <md5 HASH object @ 0x0000021C4B589A20>
print(type(hash_obj))  # -> <class '_hashlib.HASH'>
res = hash_obj.hexdigest()
print(type(res))  # -> <class 'str'>
print(res)  # -> b631e4f1254574b9c386fcbc9145d0c3

separator("Тестируем функцию md5")
hash_obj_2 = hashlib.md5(("Тестируем функцию md5").encode('utf-8'))
print(hash_obj_2)  # -> <md5 HASH object @ 0x0000021C4D53ED50>
print(type(hash_obj_2))  # -> <class '_hashlib.HASH'>
res_2 = hash_obj_2.hexdigest()
print(type(res_2))  # -> <class 'str'>
print(res_2)  # -> cb63de18e7c52d17e3b5e9743210ab74


separator("Примеры с sha")

"""Примеры с sha"""
separator("sha1")
# -------------------------------------sha1-----------------------------------#
hash_obj = hashlib.sha1(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()

print(hex_dig_res)  # -> d9536c477c646977dce73445a656a9c5e1c19d59

separator("sha224")
# ------------------------------------sha224----------------------------------#
hash_obj = hashlib.sha224(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
                # -> 5a39dff4807dc145be2cc85efa7b4c165bed383e69e0691546b2589f

print(hex_dig_res)

separator("sha256")
# ------------------------------------sha256----------------------------------#
hash_obj = hashlib.sha256(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
        # -> c54034d262f7c0b9b82ce4988f115925ee684dd39e399c9ddea0c776d27d7521

print(hex_dig_res)

separator("sha384")

# -----------------------------------sha384-----------------------------------#
hash_obj = hashlib.sha384(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
# -> 4080aa6d42e2a67c1f6307771ecbe11a23ec8283fd775d72
# 0381844cb3b9e4d038f5446f9db3123bbb4bba588c436f3f

print(hex_dig_res)

separator("sha512")

# ----------------------------------sha512------------------------------------#
hash_obj = hashlib.sha512(b'Testing sha1 func')
hex_dig_res = hash_obj.hexdigest()
# -> d4ea479e7b84b3c71416311af2e79f2919233775f86a8273eaf7e14440a
# 306df6ad9587a1d6fe624529118efa2b55740a138276a0630dc0b059066ddaec7a60f

print(hex_dig_res)


separator("Хеширование и соль")

"""Хеширование и соль"""

# Модуль uuid применяется для генерации случайного числа

salt = uuid4().hex  # -> 80740ba2a1584aa7bf96d32bbe774e54
print(salt)
print(type(salt))

# hash_algorithms = {'sha3_384', 'shake_128', 'sha224', 'blake2s', 'sha512', 'shake_256', 'sha3_512', 'sha256', 'md5', 'sha3_256', 'blake2b', 'sha384', 'sha3_224', 'sha1'}

passwd = "programmer"
# соль-часть хеша
res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
# -> efbb20c297f52672a5211f1358ad8d72907f56e1ff24cd67a6e8b4683a6a18d2
print(res)
res_1 = hashlib.sha512(salt.encode() + passwd.encode()).hexdigest()
print(res_1)

# sha1, md5 - ненадежные
# пароли одинаковые
# логины строго разные. user2, user3 - логины уникальные

separator("Массивы хеш-таблиц")

"""Простейшая хеш-таблица в Python"""

goods = dict()

goods['Диван'] = 25000
goods['Кровать'] = 7000
goods['Стул'] = 1500
# goods[([1, 2], [1, 2])] = 1500

print(goods)  # -> {'Диван': 25000, 'Кровать': 7000, 'Стул': 1500}

separator("Мемоизация, как инструмент борьбы с проблемами рекурсии")


# кэширование - это механизм
# хеширование - это средство


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


n = 8

#print(f(n))

f = memorize(f)
print(f(n))
