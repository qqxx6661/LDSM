#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhendongyang
@contact: yangzd1993@foxmail.com
@file: exp.py
@description:把运算改为类全部放在这里，为实验用
@time: 2019/1/31 10:44
"""

import Edge.client_protocol
import Cloud.server_protocol
from Edge.CONSTANT import p, fN, N
import datetime


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func(*args, **kwargs)
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = over_time - start_time
        print(start_time, over_time, '程序共计%s微秒' % total_time.microseconds)

    return int_time


class Exp:
    client_column_key_dict = {
        "1":
            {
                "cam_id": (2, 2), "time_stamp": (2, 3),
                "x_1": (2, 2), "y_1": (5, 7), "x_2": (1, 3), "y_2": (11, 13),
                "s": (3, 1), "pri": (2, 3)
            }
    }

    def encrypt(self, client_id, column_name, row_id, plain_value):
        temp = self.client_column_key_dict[client_id][column_name]
        x, y = temp[0], temp[1]
        # print("x,y = ", x, ",", y)
        v_key = Edge.client_protocol.get_v_key(x, p, row_id, y, fN, N)
        # print("v_key = ", v_key)
        v_e = Edge.client_protocol.get_v_e(plain_value, v_key, N)
        # print("v_e = ", v_e)
        return v_e

    def decrypt(self, client_id, column_name, row_id, v_e):
        temp = self.client_column_key_dict[client_id][column_name]
        x, y = temp[0], temp[1]
        # print("x,y = ", x, ",", y)
        v_key = Edge.client_protocol.get_v_key(x, p, row_id, y, fN, N)
        # print("v_key = ", v_key)
        v = Edge.client_protocol.get_v(v_e, v_key, N)
        # print("v = ", v)
        return v

    def add(self, client_id, column_name_1, column_name_2, v_1_e, v_2_e, s_e):
        temp = self.client_column_key_dict[client_id]["s"]
        x_s, y_s = temp[0], temp[1]
        print("x_s,y_s = ", x_s, ",", y_s)
        # x_c = Edge.client_protocol.generate_x()
        # y_c = Edge.client_protocol.generate_y()
        x_c = 4
        y_c = 4
        print("x_c,y_c = ", x_c, ",", y_c)

        # 数1
        # 得到j,k
        temp = self.client_column_key_dict[client_id][column_name_1]
        x_a_1, y_a_1 = temp[0], temp[1]
        print("x_a_1, y_a_1 = ", x_a_1, ",", y_a_1)
        j = Edge.client_protocol.get_update_j(y_a_1, y_c, y_s, fN, N)
        k = Edge.client_protocol.get_update_k(x_a_1, x_c, x_s, j, N)
        print("j, k:", j, k)
        # 得到中间密文c_e
        update_c_e_1 = Cloud.server_protocol.get_update_c_e(k, v_1_e, s_e, j, N)
        print("c_e_1:", update_c_e_1)

        # 数2
        temp = self.client_column_key_dict[client_id][column_name_2]
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

    def sub(self, client_id, column_name_1, column_name_2, v_1_e, v_2_e, s_e):
        temp = self.client_column_key_dict[client_id]["s"]
        x_s, y_s = temp[0], temp[1]
        print("x_s,y_s = ", x_s, ",", y_s)
        # x_c = Edge.client_protocol.generate_x()
        # y_c = Edge.client_protocol.generate_y()
        x_c = 4
        y_c = 4
        print("x_c,y_c = ", x_c, ",", y_c)

        # 数1
        # 得到j,k
        temp = self.client_column_key_dict[client_id][column_name_1]
        x_a_1, y_a_1 = temp[0], temp[1]
        print("x_a_1, y_a_1 = ", x_a_1, ",", y_a_1)
        j = Edge.client_protocol.get_update_j(y_a_1, y_c, y_s, fN, N)
        k = Edge.client_protocol.get_update_k(x_a_1, x_c, x_s, j, N)
        print("j, k:", j, k)
        # 得到中间密文c_e
        update_c_e_1 = Cloud.server_protocol.get_update_c_e(k, v_1_e, s_e, j, N)
        print("c_e_1:", update_c_e_1)

        # 数2
        temp = self.client_column_key_dict[client_id][column_name_2]
        x_a_2, y_a_2 = temp[0], temp[1]
        print("x_a_2, y_a_2 = ", x_a_2, ",", y_a_2)
        j = Edge.client_protocol.get_update_j(y_a_2, y_c, y_s, fN, N)
        k = Edge.client_protocol.get_update_k(x_a_2, x_c, x_s, j, N)
        print("j, k:", j, k)
        # 得到中间密文c_e
        update_c_e_2 = Cloud.server_protocol.get_update_c_e(k, v_2_e, s_e, j, N)
        print("c_e_2:", update_c_e_2)

        # 减法
        c_e = Cloud.server_protocol.get_sub_c_e(update_c_e_1, update_c_e_2, N)
        return x_c, y_c, c_e

    def multiple_EC(self, client_id, column_name, c, v_e):
        temp = self.client_column_key_dict[client_id][column_name]
        x_a, y_a = temp[0], temp[1]
        x_c = c * x_a
        y_c = y_a
        return x_c, y_c, v_e

    @count_time
    def encrypt_exp(self, row):
        enc_row = {}
        for i in range(600):
            for key, value in row.items():
                if key == "row_id":
                    continue
                # print("column_name:", key, "value:", value)
                enc_row[key] = self.encrypt("1", key, row["row_id"], value)
                # print("---------")
        return enc_row

    @count_time
    def decrypt_exp(self, row):
        dec_row = {}
        for i in range(600):
            for key, value in row.items():
                if key == "row_id":
                    continue
                # print("column_name:", key, "value:", value)
                dec_row[key] = self.decrypt("1", key, row["row_id"], value)
                # print("---------")
        return dec_row

    @count_time
    def add_exp(self, enc_row_dict):
        # 加法算出x_1+x_2并存入加密列
        x_c, y_c, c_e = self.add("1", "x_1", "x_2", enc_row_dict["x_1"], enc_row_dict["x_2"], enc_row_dict["s"])
        self.client_column_key_dict["1"]["x_1+x_2"] = (x_c, y_c)
        enc_row_dict["x_1+x_2"] = c_e
        print("c_e:", c_e)
        print("加法运算后将密文插入CDB，将秘钥插入DO完成")
        print("加法运算后密文列：", enc_row_dict)
        return enc_row_dict



if __name__ == "__main__":
    row_dict = {"row_id": 1, "cam_id": 1, "time_stamp": 1,
                "x_1": 23, "y_1": 94, "x_2": 194, "y_2": 471, "s": 1, "pri": 2}

    exp = Exp()

    # exp1
    enc_row_dict = exp.encrypt_exp(row_dict)
    dec_row_dict = exp.decrypt_exp(row_dict)

    # exp2
    # 明文加法
    start_time = datetime.datetime.now()  # 程序开始时间
    a = 0
    for i in range(6 * 60 * 300):
        a = a + 123456
    over_time = datetime.datetime.now()  # 程序结束时间
    total_time = over_time - start_time
    print(start_time, over_time, '程序共计%s微秒' % total_time.microseconds)
    # 明文乘法
    start_time = datetime.datetime.now()  # 程序开始时间
    a = 0
    for i in range(6 * 60 * 300):
        a = 1234 * 1234
    over_time = datetime.datetime.now()  # 程序结束时间
    total_time = over_time - start_time
    print(start_time, over_time, '程序共计%s微秒' % total_time.microseconds)
