#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: server_protocol.py
@time: 2019/1/25 18:33
"""
import math


# 像老代码一样加%n
def get_update_c_e(k, a_e, s_e, j, N):
    return int(k * a_e * math.pow(s_e, j) % N)


def get_add_c_e(a_e_plus, b_e_plus, N):
    return (a_e_plus + b_e_plus) % N

def get_minus_c_e(a_e_plus, b_e_plus, N):
    return (a_e_plus - b_e_plus) % N


if __name__ == "__main__":
    print(get_update_c_e(1998, 190, 37, 3))
    print(get_add_c_e(257114628, 19228891860, 221))
