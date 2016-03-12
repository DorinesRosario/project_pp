#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

import sys


#add conservation information to psi_blast svm format
#____________________________________________________

input_file = sys.argv[1]
input_file_2 = sys.argv[2]
output_file = sys.argv[3]


psi_blast_file = open(input_file, 'r').read().splitlines()
conservation_file = open(input_file_2, 'r').read().splitlines()

line = 1
svm_psi_blast = open(output_file, 'w')
for lines in psi_blast_file:
	for rows in conservation_file:
		print '.'
	svm_psi_blast.write(lines)
	#svm_psi_blast.write(' ')
	svm_psi_blast.write(rows)
	svm_psi_blast.write('\n')

topology_file.close()
treated_psi_blast.close()
svm_psi_blast.close()
		
