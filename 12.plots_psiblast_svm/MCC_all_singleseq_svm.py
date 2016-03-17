import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 6

MCC = [0.1226, 0.1251, 0.1016, 0.1052, 0.1378, 0.1226]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.45

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, MCC, bar_width,
                 alpha=0.4,
                 color='red',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 6, 0, 0.2])

plt.xlabel('SVM single sequence predicting helices; linear kernel default parameters')
plt.ylabel('MCC')
plt.title('MCC for single sequence predicting helices - test program')
plt.xticks(index + bar_width/2, ('global MCC', 'set_1', 'set_2', 'set_3', 'set_4', 'set_5'))
plt.tight_layout()
plt.show()