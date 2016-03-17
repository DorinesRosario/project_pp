import sys
import math


#add conservation values from psi-blast output into psi-blast svm_format
#_______________________________________________________________________


input_file_psiblast_output = sys.argv[1]
output_file_parse_psiblast_conservation = sys.argv[2]



psi_file = open(input_file_psiblast_output, 'r').readlines()[3:-6]
psi_step_1 = open(output_file_parse_psiblast_conservation, 'w')


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