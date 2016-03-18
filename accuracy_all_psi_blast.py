import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 5

accuracy = [0.7416, 0.7581, 0.7643, 0.7571, 0.3387]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, accuracy, bar_width,
                 alpha=0.4,
                 color='green',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 5, 0, 1])

plt.xlabel('SVM adding evolutionary information tested kernels')
plt.ylabel('Global kernel Accuracy')
plt.title('Accuracy of SVM kernels adding evolutionary information')
plt.xticks(index + bar_width/2, ('-t 0 -j 2.35', '-t 1 -j 2.35', '-t 2 -j 2.35', '*-c 2.5 -g 0.5', '-t 3 -j 2.35'))
plt.tight_layout()
plt.show()