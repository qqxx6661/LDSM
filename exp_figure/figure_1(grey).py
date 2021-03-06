import matplotlib.pyplot as plt
import numpy as np

size = 3
x = np.arange(size)
total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

encrypt = [0.033, 0.034, 0.067]  # 1, 60, 600摄像头加密1帧平均值
decrypt = [0.017, 0.019, 0.043]  # 1, 60, 600摄像头解密1帧平均值
error = [0.005, ] * 3  # 生成一个包含有n个值，均为0.2的list，表示允许的误差范围[-0.002,0.002]

plt.xlabel('Camera Numbers', fontsize=18.5)
plt.ylabel('Average Time Cost (ms)', fontsize=18.5)
plt.bar(x - 0.45 * width, encrypt, color="#AFEEEE", width=0.75 * width, label='Encrypt', yerr=error)
plt.bar(x + 0.45 * width, decrypt, color="#800000", width=0.75 * width, label='Decrypt', yerr=error)
plt.xticks(x, ("1", "8", "60(simulation)"), fontsize=16)
plt.yticks(fontsize=18)
plt.legend(loc='upper left', fontsize=12)


plt.show()
