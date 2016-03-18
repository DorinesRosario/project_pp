import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 8

accuracy = [0.7487, 0, 0, 0.7551, 0.7277, 0.6885, 0.6165, 0.7277]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, accuracy, bar_width,
                 alpha=0.4,
                 color='green',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 8, 0, 1])

plt.xlabel('SVM single sequence tested kernels')
plt.ylabel('Accuracy')
plt.title('Accuracy for single sequence SVM kernels')
plt.xticks(index + bar_width/2, ('-t 0', '-t 2', '-t0;-j0.27', '-t0;-j1.9', '-t0;-j2.35', '-t0;-j2.75', '-t0;-j3.6', '-t2;-j2.35'))
plt.tight_layout()
plt.show()