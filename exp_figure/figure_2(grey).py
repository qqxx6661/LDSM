import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))


text = ["10.65x", "57.62x", "54.44x"]

def autolabel_user(rects):
    for i, rect in enumerate(rects):
        height = text[i]
        plt.text(rect.get_x()+rect.get_width()/2, rect.get_height()*1.01, "%s" % height, fontsize=12, ha='center')


size = 3
x = np.arange(size)
total_width = 0.8
n = 3
width = total_width / n
x = x - (total_width - width) / 2

mingwen = [0.000124, 0.000151, 0.000154]  # 6摄像头明文运算一帧的速度
miwen = [0.00132, 0.0087, 0.0084]  # 6摄像头密文运算一帧的速度
error = [0.00001, ] * 3  # 生成一个包含有n个值，均为0.2的list，表示允许的误差范围[-0.002,0.002]

plt.xlabel('Operation', fontsize=18.5)
plt.ylabel('Average Time Cost (ms)', fontsize=18.5)
rect = plt.bar(x, miwen, color="#800000", width=0.75 * width, label='Ciphertext', yerr=error)
plt.xticks(x, ("Mul", "Add", "Sub"), fontsize=16)
plt.yticks(fontsize=18)
plt.legend(loc='upper left', fontsize=12)

autolabel_user(rect)
plt.show()
