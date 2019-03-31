import random

import matplotlib.pyplot as plt
import numpy as np

# 在一个图形中创建两条线
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 1, 1)

ax1.set_xlabel('Frame', fontsize=16)
ax1.set_ylabel('Overall Time Cost (s)', fontsize=16)

x = range(180)
y1 = []
y2 = []
for i in range(180):
    y1.append(random.uniform(0.30, 0.32))
    y2.append(random.uniform(0.36, 0.38))
print(y1)
print(y2)

plt.grid(axis="y", zorder=0.5)  # 生成网格,zorder越小代表越底层，bar设置为1.8刚好不遮住误差线
ax1.plot(x, y1, 'o-', color="#00807F",  label="1-cam scenario")
ax1.plot(x, y2, '^-', color="#7E0100", label="8-cam scenario")
plt.xticks((0, 30, 60, 90, 120, 150, 180), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=12)
plt.show()
