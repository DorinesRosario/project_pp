#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

import sys


#add svm_format information to psi-blast treated output
#______________________________________________________

input_file = sys.argv[1]
input_file_2 = sys.argv[2]
output_file = sys.argv[3]


topology_file = open(input_file, 'r').read().splitlines()
treated_psi_blast = open(input_file_2, 'r').read().splitlines()

line = 1
svm_psi_blast = open(output_file, 'w')
for lines in topology_file:
	for rows in treated_psi_blast:
		print lines, rows
	svm_psi_blast.write(lines)
	#svm_psi_blast.write(' ')
	svm_psi_blast.write(rows)
	svm_psi_blast.write('\n')

topology_file.close()
treated_psi_blast.close()
svm_psi_blast.close()
		
