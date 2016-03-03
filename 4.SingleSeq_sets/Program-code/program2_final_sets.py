#code for Task2: CREATE CROSS-VALIDATION SETS:
#the clusters from CD-hit should be randomly distribuited by the created sets; homologs sequences cannot be separeted in different sets;


#create a dictionaty from the dataset file in which: {key(head_seq): value(aa_sequence), value(structure)}

head_sequence = []
aa_sequence = [] 
structure = [] 

import linecache
#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()

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

#print 'Head sequence:', '\n', '\n', head_sequence, '\n', '\n', 'aa sequence:', '\n', '\n', aa_sequence, '\n', '\n', 'topology structure:', '\n', '\n', structure
#print 'head_sequence:', len(head_sequence), 'aa_sequece:', len(aa_sequence), 'structure:', len(structure)

file.close()

keys = head_sequence
values = (aa_sequence, structure)
seq_dataset = {x:list(y) for x,y in zip(keys, zip(*values))}
#print seq_dataset


#__________________________________________________________________



with open('prep_set_file0.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		print line
		print line[1]
		seq_name = line[1]
		if seq_name in seq_dataset:
			print 'blabla'
		
		
				


fi.close()

"""


with open('cluster_results.clstr', 'r') as fi:
	CDhit_headseq = open('CDhit_seq_name.txt', 'w+')
	for line in fi:
		row = line.split()
		if row[0] in ['0', '1', '2', '3', '4']:
			#print row
			for char in range(len(row)):
				if '>' in row[char]:
					CDhit_headseq.write(row[0])
					CDhit_headseq.write(' ')
					CDhit_headseq.write(row[char][:-3])
					CDhit_headseq.write('\n')

"""
print 'done'

#print ([item, '\n'.join(seq_dataset.get(item))] for item in seq_dataset)

