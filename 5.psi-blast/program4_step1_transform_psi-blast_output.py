#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

import sys
import math


#extracting relevant information from PSI_BLAST output file and including aa features
#____________________________________________________________________________________

input_file = sys.argv[1]
output_file = sys.argv[2]


psi_file = open(input_file, 'r').readlines()[3:-6]
psi_step_1 = open(output_file, 'w')


for line in psi_file:
	aa_line = 0
	#print line[7:72]
	#psi_step_1.write('\n')
	#psi_step_1.write('   ')
	#psi_step_1.write(line[7:72])
	#psi_step_1.write('\n')
	for prob in line.split()[2:22]:
		aa_line = aa_line + 1
		print prob
		print ('%d' %aa_line+':')
		print ('%.4f' %(float(1/(1+math.exp(-float(prob))))))
		psi_step_1.write(('%d' %aa_line+':'))
		psi_step_1.write(('%.4f' %(float(1/(1+math.exp(-float(prob)))))))
		psi_step_1.write(' ')
	psi_step_1.write('\n')


psi_file.close()
psi_step_1.close()