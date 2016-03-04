#code for Task2: CREATE CROSS-VALIDATION SETS:
#the clusters from CD-hit should be randomly distribuited by the created sets; homologs sequences cannot be separeted in different sets;


#create a dictionaty from the dataset file in which: {key(head_seq): value(aa_sequence), value(structure)}

head_sequence = []
aa_sequence = [] 
structure = [] 

import linecache
with open('stride.3line', 'r') as file:
#with open('test_stride.txt', 'r') as file:
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

#DATA SET_0

prep_set_0 = []

with open('prep_set_file0.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		#print line
		#print line[1]
		prep_set_0.append(line[1])

fi.close()

#print prep_set_0
final_setfile_0 = open('final_set_file0.txt', 'w+')
for seq_name in prep_set_0:
	if seq_name in seq_dataset:
		print seq_name
		print ('\n'.join(seq_dataset[seq_name]))
		final_setfile_0.write(seq_name)
		final_setfile_0.write('\n')
		final_setfile_0.write(('\n'.join(seq_dataset[seq_name])))
		final_setfile_0.write('\n')

final_setfile_0.close()



#__________________________________________________________________

#DATA SET_1

prep_set_1 = []

with open('prep_set_file1.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		#print line
		#print line[1]
		prep_set_1.append(line[1])

fi.close()

#print prep_set_1
final_setfile_1 = open('final_set_file1.txt', 'w+')
for seq_name in prep_set_1:
	if seq_name in seq_dataset:
		print seq_name
		print ('\n'.join(seq_dataset[seq_name]))
		final_setfile_1.write(seq_name)
		final_setfile_1.write('\n')
		final_setfile_1.write(('\n'.join(seq_dataset[seq_name])))
		final_setfile_1.write('\n')

final_setfile_1.close()


#__________________________________________________________________

#DATA SET_2

prep_set_2 = []

with open('prep_set_file2.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		#print line
		#print line[1]
		prep_set_2.append(line[1])

fi.close()

#print prep_set_2
final_setfile_2 = open('final_set_file2.txt', 'w+')
for seq_name in prep_set_2:
	if seq_name in seq_dataset:
		print seq_name
		print ('\n'.join(seq_dataset[seq_name]))
		final_setfile_2.write(seq_name)
		final_setfile_2.write('\n')
		final_setfile_2.write(('\n'.join(seq_dataset[seq_name])))
		final_setfile_2.write('\n')

final_setfile_2.close()


#__________________________________________________________________

#DATA SET_3

prep_set_3 = []

with open('prep_set_file3.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		#print line
		#print line[1]
		prep_set_3.append(line[1])

fi.close()

#print prep_set_3
final_setfile_3 = open('final_set_file3.txt', 'w+')
for seq_name in prep_set_3:
	if seq_name in seq_dataset:
		print seq_name
		print ('\n'.join(seq_dataset[seq_name]))
		final_setfile_3.write(seq_name)
		final_setfile_3.write('\n')
		final_setfile_3.write(('\n'.join(seq_dataset[seq_name])))
		final_setfile_3.write('\n')

final_setfile_3.close()


#__________________________________________________________________

#DATA SET_4

prep_set_4 = []

with open('prep_set_file4.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		#print line
		#print line[1]
		prep_set_4.append(line[1])

fi.close()

#print prep_set_4
final_setfile_4 = open('final_set_file4.txt', 'w+')
for seq_name in prep_set_4:
	if seq_name in seq_dataset:
		print seq_name
		print ('\n'.join(seq_dataset[seq_name]))
		final_setfile_4.write(seq_name)
		final_setfile_4.write('\n')
		final_setfile_4.write(('\n'.join(seq_dataset[seq_name])))
		final_setfile_4.write('\n')

final_setfile_4.close()


#__________________________________________________________________

#DATA SET_5

prep_set_5 = []

with open('prep_set_file5.txt', 'r') as fi:
	#open the new file here
	for lines in fi:
		line = lines.split()
		#print line
		#print line[1]
		prep_set_5.append(line[1])

fi.close()

#print prep_set_5
final_setfile_5 = open('final_set_file5.txt', 'w+')
for seq_name in prep_set_5:
	if seq_name in seq_dataset:
		print seq_name
		print ('\n'.join(seq_dataset[seq_name]))
		final_setfile_5.write(seq_name)
		final_setfile_5.write('\n')
		final_setfile_5.write(('\n'.join(seq_dataset[seq_name])))
		final_setfile_5.write('\n')

final_setfile_5.close()



print 'done'


