#ploting the ROC curves for three different kernels

from sklearn.metrics import roc_curve, auc
import os
import glob
import matplotlib.pyplot as plt
import random

colors = {0:'b',1:'r',2:'g'}
legend = {0:'-t 0; -j 1.9', 1:'-t 0; -j 2.35', 2:'-t 2; -j 2.35'}



os.chdir('/home/rosario/Desktop/project_pp/8.plotting/5.ROC_plot/step_3_plot_ROC_single_sequence/')


fi = 0
for files in list(glob.glob('*txt')):
	
	reader = open(files, 'r').readlines()
	dataset_features = []
	svm_predictions = []
	for line in reader:
		#print line[0:2]
		#print line[2:]
		dataset_features.append(float(line[0:2]))
		svm_predictions.append(float(line[2:]))
	#print svm_predictions
	#print dataset_features

	false_positive_rate, true_positive_rate, thresholds = roc_curve(dataset_features, svm_predictions)
	#roc_auc = auc(false_positive_rate, true_positive_rate)
	plt.plot(false_positive_rate, true_positive_rate, colors[fi], label=legend[fi])
	plt.plot([0,1], [0,1], 'r--')
	fi = fi + 1

plt.legend(loc='lower right')
plt.xlim([-0.1, 1.2])
plt.ylim([-0.1, 1.2])
plt.title('ROC: optimazing SVM kernels using single sequence information')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
