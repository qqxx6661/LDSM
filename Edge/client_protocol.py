#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: client_protocol.py
@time: 2019/1/25 17:24
"""

import random
import math
from public.enc_dec import modinv


def generate_x():
    """
    生成列密钥：x
    暂定为100以内
    :return:
    """
    return random.randint(1, 100)


def generate_y():
    """
    生成列密钥：y
    暂定为100以内
    :return:
    """
    return random.randint(1, 100)


def get_v_key(x, p, r, y, fN, N):
    """
    得到vkey
    :return:
    """
    temp = r * y % fN
    # print(temp)
    temp = math.pow(p, temp)
    # print(temp)
    temp = (x * temp) % N
    return int(temp)


def get_v_e(v, v_key, N):
    """
    得到ve
    :return:
    """
    v_key_inv = modinv(v_key, N)
    return v * v_key_inv % N


def get_v(v_e, v_key, N):
    """
    得到v
    :return:
    """
    return v_e * v_key % N


def get_update_j(y_a, y_c, y_s, fN, N):
    """
    得到键更新j
    :param y_a:
    :param y_c:
    :param y_s:
    :return:
    """
    return modinv(y_s, N) * abs(y_c - y_a) % fN


def get_update_k(x_a, x_c, x_s, j, N):
    """
    得到键更新k
    :param x_a:
    :param x_c:
    :param x_s:
    :param j:
    :param N:
    :return:
    """
    return x_a * pow(x_s, j) * modinv(x_c, N)


if __name__ == "__main__":
    # print(generate_x())
    # print(get_v_key(15, 2, 2, 13, 192, 221))
    # print(get_v_e(23, 8, 221))
    # print(get_v(141, 8, 221))
    print(get_update_j(3, 0, 1, 141, 221))
    print(get_update_k(1, 3, 3, 3, 221))
