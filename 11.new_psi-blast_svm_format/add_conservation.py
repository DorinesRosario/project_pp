#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

import sys
import math


#add conservation values to psi-blast svm_format
#_______________________________________________


input_file = sys.argv[1]
output_file = sys.argv[2]



psi_file = open(input_file, 'r').readlines()[3:-6]
psi_step_1 = open(output_file, 'w')


for line in psi_file:
	aa_line = 0
	#print line
	for char in line[-10:-6].split():
		#print char
		#print (float(char)/4.32)
		psi_step_1.write('21:')
		psi_step_1.write(str(float(char)/4.32))
		psi_step_1.write('\n')

#psi_file.close()
psi_step_1.close()