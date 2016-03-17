import sys
import math


#add conservation values from psi-blast output into psi-blast svm_format
#_______________________________________________________________________


input_file_psiblast_output = sys.argv[1]
output_file_parse_psiblast_add0 = sys.argv[2]


psi_file = open(input_file_psiblast_output, 'r').readlines()[3:-6]
psi_step_1 = open(output_file_parse_psiblast_add0, 'w')


for line in psi_file:
	psi_step_1.write('0')
	psi_step_1.write(' ')
	psi_step_1.write(line)
	#psi_step_1.write('\n')

#psi_file.close()
psi_step_1.close()