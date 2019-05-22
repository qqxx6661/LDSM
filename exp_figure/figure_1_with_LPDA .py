import matplotlib.pyplot as plt
import numpy as np


def autolabel_user_1(rects):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if i == 2:
            plt.text(rect.get_x() + rect.get_width() / 2., 1.01 * height, "%s" % float(height))
        else:
            plt.text(rect.get_x(), height + 0.03, "%s" % float(height))

def autolabel_user_2(rects):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if i == 2:
            plt.text(rect.get_x() + rect.get_width() / 2., 1.01 * height, "%s" % float(height))
        else:
            plt.text(rect.get_x(), height + 0.03, "%s" % float(height))

size = 2
x = np.arange(size)
total_width, n = 0.6, 2
width = total_width / n
x = x - (total_width - width) / 2

Plain_text = [0.798, 0.062]
Ours = [0.852, 0.083]  # 聚合任务
LPDA = [0.906, 0.156]
error = [0.02, ] * 2  # 生成一个包含有n个值，均为0.003的list，表示允许的误差范围[-0.002,0.002]

plt.xlabel('Computational Entity', fontsize=16)
plt.ylabel('Average Time Cost (ms)', fontsize=16)
rect1 = plt.bar(x - 0.7 * width, Plain_text, fc='#FFA245', width=0.5 * width, label='Plaintext', yerr=error, capsize=8,
        hatch="\\\\\\", edgecolor="k", zorder=1.8)
rect2 = plt.bar(x, Ours, fc='#FF4D00', width=0.5 * width, label='Ours', yerr=error, capsize=8,
        hatch="xxx", edgecolor="k", zorder=1.8)
rect3 = plt.bar(x + 0.7 * width, LPDA, fc='#600000', width=0.5 * width, label='LPDA', yerr=error, capsize=8,
        hatch="---", edgecolor="k", zorder=1.8)
plt.xticks(x, ("Edge node", "Cloud server"), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis="y", zorder=0.5)  # 生成网格,zorder越小代表越底层，bar设置为1.8刚好不遮住误差线

autolabel_user_1(rect1)
autolabel_user_2(rect2)
autolabel_user_2(rect3)
plt.show()
