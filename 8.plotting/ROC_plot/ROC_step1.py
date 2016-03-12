#PREPARING THE FILES FORMAT TO PLOT ROC
#______________________________________


#(program 4 step 3)

"""
import sys

input_file = sys.argv[1]
input_file_2 = sys.argv[2]
output_file = sys.argv[3]
"""


file_set_svm = open ('all.svm', 'r').read().splitlines()
file_set_pred = open ('all.svm.pred', 'r').read().splitlines()

line = 1
roc_prep = open('roc_step1.txt', 'w' )
for feature in file_set_svm:
	for prediction in file_set_pred:
		line = line + 1
		#print '.'
		#print feature[0:2], prediction
	roc_prep.write(feature[0:2])
	roc_prep.write(' ')
	roc_prep.write(prediction)
	roc_prep.write('\n')

file_set_svm.close()
file_set_pred.close()
roc_prep.close()