import hashlib


s = hashlib.sha1(b'Hello World!').hexdigest()

print(s)

salt = b'sdflkjfdfkjsdkgnrkgnrg'  # Добавим соль

sms = hashlib.sha1(salt + bytes(s.encode('utf-8'))).hexdigest()

print(sms)
