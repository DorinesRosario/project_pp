"""
import sys

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
"""

bananas = ['banana','bla', 'casa', 'escola']
mesa = ['cinco', 'seis', 'sete', 'oito']

print bananas
print bananas[0]
print mesa 
print mesa[1]


file_novo = open ('file.novo.txt', 'w')
for i in bananas and mesa:
	file_novo.write(bananas[i])
	file_novo.write(' ')
	file_novo.write(mesa[i])
	file_novo.write('\n')