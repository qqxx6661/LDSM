import random

import matplotlib.pyplot as plt
import numpy as np

# 在一个图形中创建两条线
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(1, 1, 1)

ax1.set_xlabel('Number of Group Numbers', fontsize=18)
ax1.set_ylabel('Time (s)', fontsize=18)

x = range(100)
y1 = [4.15] * 100
y2 = [7.8356] * 100
print(y1)
print(y2)

ax1.plot(x, y1, label="Knox", linewidth = 2)
ax1.plot(x, y2, label="Ours", linewidth = 2)
plt.xticks((0, 20, 40, 60, 100), fontsize=16)
plt.yticks((0,2,4,6,8), fontsize=18)
plt.legend()
plt.show()
