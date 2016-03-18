import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 8

MCC = [-0.0059, 0, 0, 0.1529, 0.1528, 0.1446, 0.1773, 0.1528]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, MCC, bar_width,
                 alpha=0.4,
                 color='red',
                 error_kw=error_config)

autolabel(rect)

plt.axis([0, 8, 0, 0.5])

plt.xlabel('SVM single sequence tested kernels')
plt.ylabel('MCC')
plt.title('Global MCC for single sequence SVM kernels')
plt.xticks(index + bar_width/2, ('-t 0', '-t 2', '-t0;-j0.27', '-t0;-j1.9', '-t0;-j2.35', '-t0;-j2.75', '-t0;-j3.6', '-t2;-j2.35'))
plt.tight_layout()
plt.show()