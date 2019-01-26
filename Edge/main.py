#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: main.py
@time: 2019/1/25 21:26
"""

import Edge.client_protocol
import Cloud.server_protocol
from Edge.CONSTANT import p, fN, N

# 每个客户端ck不同，暂时只有1个客户端。
client_column_key_dict = {
    "1":
        {
            "cam_id": (2, 2), "time_stamp": (2, 3),
            "x_1": (2, 2), "y_1": (5, 7), "x_2": (1, 3), "y_2": (11, 13),
            "s": (3, 1), "pri": (2, 3)
        }
}


def encrypt(client_id, column_name, row_id, plain_value):
    temp = client_column_key_dict[client_id][column_name]
    x, y = temp[0], temp[1]
    print("x,y = ", x, ",", y)
    v_key = Edge.client_protocol.get_v_key(x, p, row_id, y, fN, N)
    print("v_key = ", v_key)
    v_e = Edge.client_protocol.get_v_e(plain_value, v_key, N)
    print("v_e = ", v_e)
    return v_e


def decrypt(client_id, column_name, row_id, v_e):
    temp = client_column_key_dict[client_id][column_name]
    x, y = temp[0], temp[1]
    print("x,y = ", x, ",", y)
    v_key = Edge.client_protocol.get_v_key(x, p, row_id, y, fN, N)
    print("v_key = ", v_key)
    v = Edge.client_protocol.get_v(v_e, v_key, N)
    print("v = ", v)
    return v


def add(client_id, column_name_1, column_name_2, v_1_e, v_2_e, s_e):
    temp = client_column_key_dict[client_id]["s"]
    x_s, y_s = temp[0], temp[1]
    print("x_s,y_s = ", x_s, ",", y_s)
    # x_c = Edge.client_protocol.generate_x()
    # y_c = Edge.client_protocol.generate_y()
    x_c = 4
    y_c = 4
    print("x_c,y_c = ", x_c, ",", y_c)

    # 数1
    # 得到j,k
    temp = client_column_key_dict[client_id][column_name_1]
    x_a_1, y_a_1 = temp[0], temp[1]
    print("x_a_1, y_a_1 = ", x_a_1, ",", y_a_1)
    j = Edge.client_protocol.get_update_j(y_a_1, y_c, y_s, fN, N)
    k = Edge.client_protocol.get_update_k(x_a_1, x_c, x_s, j, N)
    print("j, k:", j, k)
    # 得到中间密文c_e
    update_c_e_1 = Cloud.server_protocol.get_update_c_e(k, v_1_e, s_e, j, N)
    print("c_e_1:", update_c_e_1)

    # 数2
    temp = client_column_key_dict[client_id][column_name_2]
    x_a_2, y_a_2 = temp[0], temp[1]
    print("x_a_2, y_a_2 = ", x_a_2, ",", y_a_2)
    j = Edge.client_protocol.get_update_j(y_a_2, y_c, y_s, fN, N)
    k = Edge.client_protocol.get_update_k(x_a_2, x_c, x_s, j, N)
    print("j, k:", j, k)
    # 得到中间密文c_e
    update_c_e_2 = Cloud.server_protocol.get_update_c_e(k, v_2_e, s_e, j, N)
    print("c_e_2:", update_c_e_2)

    # 加法
    c_e = Cloud.server_protocol.get_add_c_e(update_c_e_1, update_c_e_2, N)
    return x_c, y_c, c_e


if __name__ == "__main__":

    row_dict = {"row_id": 1, "cam_id": 1, "time_stamp": 1,
                "x_1": 23, "y_1": 94, "x_2": 194, "y_2": 471, "s": 1, "pri": 2}

    enc_row_dict = {}

    dec_row_dict = {}

    # 加密
    for key, value in row_dict.items():
        if key == "row_id":
            continue
        print("column_name:", key, "value:", value)
        enc_row_dict[key] = encrypt("1", key, row_dict["row_id"], value)
        print("---------")

    # 加密后
    print("加密后列：", enc_row_dict)

    # 加法算出x_1+x_2并存入加密列
    x_c, y_c, c_e = add("1", "x_1", "x_2", enc_row_dict["x_1"], enc_row_dict["x_2"], enc_row_dict["s"])
    client_column_key_dict["1"]["x_1+x_2"] = (x_c, y_c)
    enc_row_dict["x_1+x_2"] = c_e
    print("c_e:", c_e)
    print("Add finish, insert encrypted value into CDB, column key into DO")

    # 加法运算后
    print("加法运算后：", enc_row_dict)

    # 乘法运算（x_1和y_1乘-1）并存入加密列


    # 求和运算并存入加密列


    # 解密
    for key, value in enc_row_dict.items():
        if key == "row_id":
            continue
        print("column_name:", key, "value:", value)
        dec_row_dict[key] = decrypt("1", key, row_dict["row_id"], value)
        print("---------")

    # 解密后
    print("解密后列：", dec_row_dict)
