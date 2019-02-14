import matplotlib.pyplot as plt
import numpy as np


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()*1.05, 1.03 * height, "%s" % float(height))


text = ["10.65x", "57.62x", "54.44x"]


def autolabel_user(rects):
    for i, rect in enumerate(rects):
        height = text[i]
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() * 1.01, "%s" % height, fontsize=12, ha='center')


size = 2
x = np.arange(size)
total_width = 0.8
n = 2
width = total_width / n
x = x - (total_width - width) / 2

mingwen = [0.000124, 0.000151, 0.000154]  # 6摄像头明文运算一帧的速度
miwen = [0, 20]  # 6摄像头密文运算一帧的速度
error = [0.00001, ] * 3  # 生成一个包含有n个值，均为0.2的list，表示允许的误差范围[-0.002,0.002]

# plt.xlabel(fontsize=18.5)
plt.ylabel('The number of the same ip', fontsize=18.5)
rect = plt.bar(x, miwen, width=0.4 * width, color=['r', 'b'])
plt.xticks(x, ("with tor", "without tor"), fontsize=16)
plt.yticks((0, 5, 10, 15, 20), fontsize=18)
plt.legend(loc='upper left', fontsize=12)

# autolabel(rect)
plt.show()
