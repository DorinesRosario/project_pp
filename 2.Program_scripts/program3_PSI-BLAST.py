#TASK 4: PSI-BLAST input_files

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


head_and_AAsequence = {}
#tuple_headseq = tuple(head_sequence)
#tuple_aaseq = tuple(aa_sequence)
head_and_AAsequence = dict(zip(head_sequence, aa_sequence))

#print head_and_AAsequence


n = 1 #number of sequences per file
sequences = (head_and_AAsequence.items()[i:i+n] for i in xrange(0, len(head_and_AAsequence),n))
for ind, sec in enumerate(sequences):
	with open('psi-blast_input_{0}.fasta'.format(ind), 'w') as new_file:
		for k, v in sec:
			new_file.write('{}\n{}\n'.format(k,v))



