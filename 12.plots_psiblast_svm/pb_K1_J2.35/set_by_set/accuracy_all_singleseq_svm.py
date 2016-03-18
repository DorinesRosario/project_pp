import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 6

accuracy = [0.7581, 0.7606, 0.7549, 0.7638, 0.7517, 0.7582]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, accuracy, bar_width,
                 alpha=0.4,
                 color='green',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 6, 0, 1])

plt.xlabel('SVM multiple sequence evol_info; -t 1 -j 2.35 parameters')
plt.ylabel('Accuracy')
plt.title('Accuracy selecting -t 1 -j 2.35 in SVM adding evolutionary information')
plt.xticks(index + bar_width/2, ('global Accuracy', 'set_1', 'set_2', 'set_3', 'set_4', 'set_5'))
plt.tight_layout()
plt.show()