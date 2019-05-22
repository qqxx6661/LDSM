import numpy as np
import matplotlib.pyplot as plt

x = (0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
y1 = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
y2 = [i * 2 for i in y1]
y3 = [i * 4 for i in y1]

print(y1)
print(y2)
print(y3)
plt.plot(x, y1, marker='o', c='r', label='Ours')
plt.plot(x, y2, marker='o', c='b', label='LPDA')
plt.plot(x, y3, marker='o', c='g', label='AggBPE')
plt.xlabel('IoT device number', fontsize=13)
plt.ylabel('Communication overhead (bits) ($10^{6}$)', fontsize=13)
# plt.legend(loc="lower left", bbox_to_anchor=(0.35, 0.01))



plt.legend()
plt.grid(linestyle='--')
plt.show()