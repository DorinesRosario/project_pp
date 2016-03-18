import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 5

MCC = [0.1534, 0.1592, 0.1562, 0.1498, 0.1389]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, MCC, bar_width,
                 alpha=0.4,
                 color='red',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 5, 0, 0.5])

plt.xlabel('SVM single sequence -t 0 -j 1.9')
plt.ylabel('MCC')
plt.title('MCC selecting -t 0 -j 1.9 in SVM single sequence')
plt.xticks(index + bar_width/2, ('set_1', 'set_2', 'set_3', 'set_4', 'set_5'))
plt.tight_layout()
plt.show()