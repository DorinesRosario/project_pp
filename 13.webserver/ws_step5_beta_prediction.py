import sys
import math


#add conservation values from psi-blast output into psi-blast svm_format
#_______________________________________________________________________


svm_pred_output = sys.argv[1]
beta_prediction = sys.argv[2]


psi_file = open(svm_pred_output, 'r').readlines()[3:-6]
psi_step_1 = open(beta_prediction, 'w')

for prediction in psi_file:
	if float(prediction) > 0:
		print 'S'
		psi_step_1.write('S')
	else: 
		print '-'
		psi_step_1.write('-')

#psi_file.close()
psi_step_1.close()