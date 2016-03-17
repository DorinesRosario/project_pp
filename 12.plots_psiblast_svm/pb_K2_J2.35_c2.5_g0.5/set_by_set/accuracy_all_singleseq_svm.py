import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 6

accuracy = [0.7571, 0.7863, 0.7558, 0.7614, 0.7493, 0.7571]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.45

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, accuracy, bar_width,
                 alpha=0.4,
                 color='green',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 6, 0, 0.9])

plt.xlabel('SVM multiple sequence evol_info; -t 2 -j 2.35 -c 2.5 -g 0.5 parameters')
plt.ylabel('Accuracy')
plt.title('Accuracy: -t 2 -j 2.35 -c 2.5 -g 0.5 in SVM adding evolutionary information')
plt.xticks(index + bar_width/2, ('global Accuracy', 'set_1', 'set_2', 'set_3', 'set_4', 'set_5'))
plt.tight_layout()
plt.show()