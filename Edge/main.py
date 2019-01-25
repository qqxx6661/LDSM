#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: main.py
@time: 2019/1/25 21:26
"""

import Edge.client_protocol
from Edge.CONSTANT import p, fN, N

# 每个客户端ck不同，暂时只有1个客户端。
client_column_key_dict = {
    "1":
        {
            "cam_id": (2, 2), "time_stamp": (2, 3),
            "x_1": (3, 5), "y_1": (5, 7), "x_2": (7, 11), "y_2": (11, 13),
            "s": (13, 17), "pri": (17, 19)
        }
}


def encrypt(client_id, column_name, row_id, plain_value):
    temp = client_column_key_dict[client_id][column_name]
    x = temp[0]
    y = temp[1]
    print("x,y = ", x, y)
    v_key = Edge.client_protocol.get_v_key(x, p, row_id, y, fN, N)
    print("v_key = ", v_key)
    v_e = Edge.client_protocol.get_v_e(plain_value, v_key, N)
    print("v_e = ", v_e)
    return v_e


if __name__ == "__main__":

    # 加密行例子
    row_dict = {"row_id": 1, "cam_id": 1, "time_stamp": 1,
                "x_1": 23, "y_1": 94, "x_2": 194, "y_2": 471, "s": 1, "pri": 2}

    enc_row_dict = {}

    for k, v in row_dict.items():
        if k == "row_id":
            continue
        print("---------")
        print("column_name:", k, "value:", v)
        enc_row_dict[k] = encrypt("1", k, row_dict["row_id"], v)

    # 加密后例子
    print(enc_row_dict)

    # 加法
