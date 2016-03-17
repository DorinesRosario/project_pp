import sys
import math


#extracting relevant information from PSI_BLAST output file considering aa
#_________________________________________________________________________


input_file_psiblast_output = sys.argv[1]
output_file_parse_psiblast_aa = sys.argv[2]


psi_file = open(input_file_psiblast_output, 'r').readlines()[3:-6]
psi_step_1 = open(output_file_parse_psiblast_aa, 'w')


for line in psi_file:
	aa_line = 0
	#print line[7:72]
	#psi_step_1.write('\n')
	#psi_step_1.write('   ')
	#psi_step_1.write(line[7:72])
	#psi_step_1.write('\n')
	for prob in line.split()[2:22]:
		aa_line = aa_line + 1
		#print prob
		#print ('%d' %aa_line+':')
		#print ('%.4f' %(float(1/(1+math.exp(-float(prob))))))
		psi_step_1.write(('%d' %aa_line+':'))
		psi_step_1.write(str(float(1/(1+math.exp(-float(prob))))))
		psi_step_1.write(' ')
	psi_step_1.write('\n')


#psi_file.close()
psi_step_1.close()