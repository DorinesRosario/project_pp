#code for Task2: CREATE CROSS-VALIDATION SETS:
#the clusters from CD-hit should be randomly distribuited by the created sets; homologs sequences cannot be separeted in different sets;


#create a dictionaty from the dataset file in which: {key(head_seq): value(aa_sequence), value(structure)}


head_sequence = []
aa_sequence = [] 
structure = [] 

import linecache
#with open('stride.3line', 'r') as fil:
with open('test_stride.txt', 'r') as fil:
	lines = fil.read().splitlines()
line = 1

dataset_seqs = {}
for line in range(0, int(len(lines)),3):
	dataset_seqs[lines[line]] = (lines[line + 1], lines[line + 2])

#print dataset_seqs


#for each set_file for cross validation use the dictionary to obtain the file format: head_seq; aa_seq; structure

