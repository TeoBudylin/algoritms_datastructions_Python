# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

str = 'hellohelloworld'
hash_set = set()
for i in range(0, len(str)):
    for j in range(1, len(str) - 1):
        sub_str = str[i:j]
        sub_str_hash = hashlib.sha1(b"{sub_str}")
        hash_set.add(sub_str_hash)

print(len(hash_set))