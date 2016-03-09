#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION


#treat the stride.3line file to add information to psi-blast transformed output
#______________________________________________________________________________


head_sequence = []
aa_sequence = [] 
structure = [] 


import linecache
with open('stride.3line', 'r') as f:
	lines = f.readlines()
line = 1
for row in lines:
	row = row.strip()
	if (line%3 == 1):
		line = line + 1
		head_sequence.append(row)
	elif (line%3 == 2):
		line = line + 1
		aa_sequence.append(row)
	elif (line%3 == 0):
		line = line + 1
		structure.append(row)

f.close()
print structure
print head_sequence



#create 1 seq_structure/ 1 file
#______________________________

seq_num = 0
file_num = ''
for seq_structure in structure:
	file_num += 'sequence'
	file_num += str(seq_num)
	with open(file_num+'.txt', 'w') as strct_file:
		strct_file.write(seq_structure)
		seq_num = seq_num + 1
		file_num = ''




#create 1 seq_name/ 1 file
#_________________________

seq_num = 0
file_num = ''
for seq_name in head_sequence:
	file_num += 'seq_name'
	file_num += str(seq_num)
	with open(file_num+'.txt', 'w') as name_file:
		name_file.write(seq_name)
		seq_num = seq_num + 1
		file_num = ''
