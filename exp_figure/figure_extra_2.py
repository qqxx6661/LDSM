import numpy as np
import matplotlib.pyplot as plt

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
y2 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
y4 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
y3 = [i * 4 for i in y1]

print(y1)
print(y2)
print(y3)
plt.plot(x, y4, marker='o', c='r', label='Ours')
plt.plot(x, y2, marker='o', c='b', label='LPDA')
plt.plot(x, y3, marker='o', c='g', label='AggBPE')
plt.xlabel('Subset number', fontsize=13)
plt.ylabel('Communication overhead (bits) ($10^{6}$)', fontsize=13)
# plt.legend(loc="lower left", bbox_to_anchor=(0.35, 0.01))
plt.xticks(x, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), fontsize=13)
plt.legend()
plt.grid(linestyle='--')
plt.show()
