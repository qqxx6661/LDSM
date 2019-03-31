import matplotlib.pyplot as plt
import numpy as np


def autolabel_user_1(rects):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if i == 2:
            plt.text(rect.get_x() + rect.get_width() / 2., 1.01 * height, "%s" % float(height))
        else:
            plt.text(rect.get_x() + rect.get_width() / 2., 1.02 * height, "%s" % float(height))

def autolabel_user_2(rects):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if i == 2:
            plt.text(rect.get_x() + rect.get_width() / 2., 1.01 * height, "%s" % float(height))
        else:
            plt.text(rect.get_x() + rect.get_width() / 2., 1.02 * height, "%s" % float(height))

size = 3
x = np.arange(size)
total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

encrypt = [0.033, 0.034, 0.067]  # 1, 60, 600摄像头加密1帧平均值
decrypt = [0.017, 0.019, 0.043]  # 1, 60, 600摄像头解密1帧平均值
error = [0.003, ] * 3  # 生成一个包含有n个值，均为0.003的list，表示允许的误差范围[-0.002,0.002]

plt.xlabel('Camera Numbers', fontsize=16)
plt.ylabel('Average Time Cost (ms)', fontsize=16)
rect1 = plt.bar(x - 0.45 * width, encrypt, fc='#00807F', width=0.75 * width, label='Encrypt', yerr=error, capsize=8,
        hatch="\\\\\\", edgecolor="k", zorder=1.8)
rect2 = plt.bar(x + 0.45 * width, decrypt, fc='#7E0100', width=0.75 * width, label='Decrypt', yerr=error, capsize=8,
        hatch="xxx", edgecolor="k", zorder=1.8)
plt.xticks(x, ("1", "8", "60(simulation)"), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(loc='upper left', fontsize=12)
plt.grid(axis="y", zorder=0.5)  # 生成网格,zorder越小代表越底层，bar设置为1.8刚好不遮住误差线

autolabel_user_1(rect1)
autolabel_user_2(rect2)
plt.show()
