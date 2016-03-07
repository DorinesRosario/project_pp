#TASK 4: 

import math




#working stride_dataset file information
#_______________________________________

head_sequence = []
aa_sequence = [] 
structure = [] 


import linecache
#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()
#head_sequence_file = open('head_sequence_file.txt', 'w+')
#aa_sequence_file = open('aa_sequence_file.txt', 'w+')
#structure_file = open('structure_file.txt', 'w+')

line = 1
for row in lines:
	row = row.strip()
	if (line%3 == 1):
		#head_sequence_file.write(row)
		line = line + 1
		head_sequence.append(row)
	elif (line%3 == 2):
		#aa_sequence_file.write(row)
		line = line + 1
		aa_sequence.append(row)
	elif (line%3 == 0):
		#structure_file.write(row)
		line = line + 1
		structure.append(row)

#head_sequence_file.close()
#aa_sequence_file.close()
#structure_file.close()

structure_list = []
for topology in structure:
	strt = list(topology)
	#print strt
	structure_list.append(strt)

features = {'S':'+1 ', 'H':'-1 ', 'C':'-1 '}




#extracting relevant information from psi-blast output
#_____________________________________________________

psi_blast = []
test_psi = []
psi_blast_value = []

psi_file = open('psi-blast_input_0.psi', 'r').readlines()[3:-6]
test_psi.append(str(psi_file))

line_num = 0
feat_count = 0
for line in psi_file:
	print line
	print line[8:73]
	print line[7:69]
	print line [10:69]
	#psi_blast.append(line[10:69])
	#print features[structure_list[feat_count][line_num]]
	prob_num = 1
	for prob in line[10:69].split(): 
		#print ('%d' %prob_num+':'+'%.4f' %(float(1/(1+math.exp(-float(prob))))))
		psi_blast_value.append(str('%d' %prob_num+':'+'%.4f' %(float(1/(1+math.exp(-float(prob)))))))
		prob_num = prob_num + 1
	line_num = line_num + 1
	feat_count = feat_count + 1
	

#print psi_blast
#print test_psi
#print psi_blast_value




#using arrays for psi-blast treated-output and seq_structures:
#_____________________________________________________________



#print 'Head sequence:', '\n', '\n', head_sequence, '\n', '\n', 'aa sequence:', '\n', '\n', aa_sequence, '\n', '\n', 'topology structure:', '\n', '\n', structure
#print 'head_sequence:', len(head_sequence), 'aa_sequece:', len(aa_sequence), 'structure:', len(structure), 'structure_list:' len(structure_list)

"""


for (feature, item) in enumerate(structure_list):
	for prob in 











#extracting relevant information from PSI_BLAST output file and including aa features
#____________________________________________________________________________________


psi_file = open('psi-blast_input_0.psi', 'r').readlines()[3:-6]
psi_step_1 = open('psi_blast_1step.txt', 'w')

psi_step_1.write('\n')

aa_line = 0
for line in psi_file:
	aa_line = aa_line + 1
	#print line[7:72]
	psi_step_1.write('\n')
	#psi_step_1.write(line[7:72])
	#psi_step_1.write('\n')
	for prob in line[7:72].split():
		print prob
		print ('%.4f' %(float(1/(1+math.exp(-float(prob))))))
		psi_step_1.write(('%.4f' %(float(1/(1+math.exp(-float(prob)))))))


psi_file.close()
psi_step_1.close()


#___________________________________________
test_psi = []

psi_file = open('psi-blast_input_0.psi', 'r').read()
#for lines in psi_file:
	#print lines
test_psi.append(str(psi_file))
print test_psi



"""

















print 'done'