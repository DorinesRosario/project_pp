import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 5

accuracy = [0.7584, 0.7728, 0.7605, 0.7039, 0.7621]

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

plt.xlabel('SVM single sequence -t 0 -j 1.9')
plt.ylabel('Accuracy')
plt.title('Accuracy selecting -t 0 -j 1.9 in SVM single sequence')
plt.xticks(index + bar_width/2, ('set_1', 'set_2', 'set_3', 'set_4', 'set_5'))
plt.tight_layout()
plt.show()