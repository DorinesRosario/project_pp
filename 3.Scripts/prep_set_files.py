#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

import sys


#adapt prep set files to be used for psi-blast svm_fomart
#________________________________________________________

input_file = sys.argv[1]
output_file = sys.argv[2]


with open(input_file, 'r') as set_file0:
	set0 = set_file0.read().splitlines()
	with open(output_file, 'w') as out:
		for seqs0 in set0:
			print seqs0
			print seqs0[2:]
			out.write(seqs0[2:])
			out.write('\n')

