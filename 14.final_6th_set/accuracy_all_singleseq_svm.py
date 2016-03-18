import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 1

accuracy = [0.7889]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.2

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, accuracy, bar_width,
                 alpha=0.4,
                 color='green',
                 error_kw=error_config)

autolabel(rect)

plt.axis([-0.2, 0.5, 0, 1])

plt.xlabel('SVM -t 0 -j 2.35 parameters: final model')
plt.ylabel('Accuracy')
plt.title('Accuracy for the final model: -t 0 -j 2.35 SVM parameters')
plt.xticks(index + bar_width/2, ('Final model -t 0 -j 2.35'))
plt.tight_layout()
plt.show()