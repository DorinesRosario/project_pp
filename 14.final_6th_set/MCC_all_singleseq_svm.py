import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 2

MCC = [0.4079, 0.7889]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, MCC, bar_width,
                 alpha=0.4,
                 color='yellow',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 6, 0, 1])

#plt.xlabel('SVM -t 0 -j 2.35 parameters: final model')
plt.ylabel('SVM -t 0 -j 2.35 parameters')
plt.title('MCC  for the final model                                                                   .')
plt.xticks(index + bar_width/2, ('MCC', 'Accuracy'))
plt.tight_layout()
plt.show()