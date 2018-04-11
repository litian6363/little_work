#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ID 转 MID
"""

__author__ = 'LiTian'


def id2mid(my_id):
    mid = ''
    while True:
        if len(my_id) > 7:
            a = base62_encode(int(my_id[-7:]))
            if len(a) < 4:
                a = '0' * (4 - len(a)) + a
            mid = a + mid
            my_id = my_id[:-7]
        else:
            mid = base62_encode(int(my_id)) + mid
            break
    return mid


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(num, alphabet=ALPHABET):
    """10进制转62进制"""

    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """62进制转10进制"""

    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


if __name__ == '__main__':
    a = '1909839587'
    print(id2mid(a))
    print(base62_decode(id2mid(a)))
