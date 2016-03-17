import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 6

MCC = [0.3288, 0.4026, 0.3124, 0.3080, 0.3055, 0.3193]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.45

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, MCC, bar_width,
                 alpha=0.4,
                 color='red',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 6, 0, 0.6])

plt.xlabel('SVM multiple sequence evol_info; -t 2 -j 2.35 -c 2.5 -g 0.5 parameters')
plt.ylabel('MCC')
plt.title('MCC: -t 2 -j 2.35 -c 2.5 -g 0.5 in SVM adding evolutionary information')
plt.xticks(index + bar_width/2, ('global MCC', 'set_1', 'set_2', 'set_3', 'set_4', 'set_5'))
plt.tight_layout()
plt.show()