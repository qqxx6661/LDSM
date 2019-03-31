import matplotlib.pyplot as plt
import numpy as np


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.03 * height, "%s" % float(height), ha='center')


text = ["10.65x", "57.62x", "54.44x"]


def autolabel_user(rects):
    for i, rect in enumerate(rects):
        height = text[i]
        if i == 0:  # 由于第一个数字贴着柱子，特殊照顾
            plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() * 1.16, "%s" % height, fontsize=10,
                     ha='center')
        else:
            plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() * 1.02, "%s" % height, fontsize=10, ha='center')


size = 3
x = np.arange(size)
total_width = 0.8
n = 3
width = total_width / n
x = x - (total_width - width) / 2

mingwen = [0.000124, 0.000151, 0.000154]  # 6摄像头明文运算一帧的速度
miwen = [0.00132, 0.0087, 0.0084]  # 6摄像头密文运算一帧的速度
error = [0.0001, ] * 3  # 生成一个包含有n个值，均为0.00001的list，表示允许的误差范围[-0.002,0.002]

plt.xlabel('Operation', fontsize=16)
plt.ylabel('Average Time Cost (ms)', fontsize=16)
rect = plt.bar(x, miwen, color="#FF8001", width=0.75 * width, label='Ciphertext', capsize=8, edgecolor="k", zorder=1.8, yerr=error)
plt.xticks(x, ("Mul", "Add", "Sub"), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(loc='upper left', fontsize=12)
plt.grid(axis="y", zorder=0.5)  # 生成网格,zorder越小代表越底层，bar设置为1.8刚好不遮住误差线

autolabel_user(rect)
plt.show()
