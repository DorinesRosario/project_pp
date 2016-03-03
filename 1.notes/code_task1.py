#code for Task1: EXTRACT FEATURES FROM DATABASE: 
#features that are positive/negative examples for my predicter(beta_sheets)

amino_acids_number = {'R':1, 'K':2, 'D':3, 'E':4, 'Q':5, 'N':6, 'H':7, 'S':8, 'T':9, 'Y':10, 'C':11, 'M':12, 'W':13, 'A':14, 'I':15, 'L':16, 'F':17, 'V':18, 'P':19, 'G':20}

head_sequences = []
aa_sequeces = []
structures = []

#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()

for line in lines:
	line = line.strip()
	if '>' in line:
		head_sequences.append(line)
	if '>' not in line:
		if 'A' in line: #must find a better way of doing it, 3 sequences missing 'A'
			aa_sequeces.append(line)
		else:
			structures.append(line)

#print 'Head sequences:', '\n', '\n', head_sequences, '\n', '\n', 'aa sequences:', '\n', '\n', aa_sequeces, '\n', '\n', 'Topology structures:', '\n', '\n', structures
print 'head_sequences:', len(head_sequences), 'aa_sequeces:', len(aa_sequeces), 'structures:', len(structures)


#creating a dictionary from aa sequences and respective structures, to then extract features of interest 
# !!!!!!!!!!! maybe dictionary should contain "head sequence", to be used to perfomr the sets for cross-validation (considering CD-hit [homology] results)
# NOTE: homologs should be placed in the same set for cross-validation;

#dictionary = dict(zip(aa_sequeces, structures))
#print dictionary

#extracting features of interest: in structure topology 'S'= positive example; 'H' and 'C' = negative examples, and presenting the position of the aa in the sequence;
#format: one example per line; + or - example (+ or - 1); aa position in sequence:1 ---> +1 8:1 (new line) -1 2:1;

for string in structures:
	for i in range(len(structures)):
		if i == 'S':
			print '+1 ', aa_sequeces[i],':1' '\n'
		elif i == 'C':
			print '-1 ', aa_sequeces[i],':1' '\n'
		else:
			print '-1 ', aa_sequeces[i],':1' '\n'

	#CORRECT: it is not printing the position in aa_sequence; it is repeating the print (it is inside of the loop!)
	#ver "operações" entre listas.