#code for Task1: EXTRACT FEATURES FROM DATABASE: 
#features that are positive/negative examples for my predicter(beta_sheets)
import sys

head_sequence = []
aa_sequence = [] 
structure = [] 

input_file = sys.argv[1]
output_file = sys.argv[2]
import linecache
with open(input_file, 'r') as file:
#with open('test_stride.txt', 'r') as file:
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

# note: !!it is adding the rows in the files without space btw them!! correct it if I need this files
#head_sequence_file.close()
#aa_sequence_file.close()
#structure_file.close()


#print 'Head sequence:', '\n', '\n', head_sequence, '\n', '\n', 'aa sequence:', '\n', '\n', aa_sequence, '\n', '\n', 'topology structure:', '\n', '\n', structure
print 'head_sequence:', len(head_sequence), 'aa_sequece:', len(aa_sequence), 'structure:', len(structure)



#{seq1:str1, seq2:str2, seq3:str3 ...}; I want char by char {char1seq1:char1str1, char2seq1:char2str1 ...}
#to break my sequences into char, array, to then evaluate and study correspondent ones

aa_seq_list = []
for sequence in aa_sequence:
	aa_seq = list(sequence)
	#print aa_seq
	aa_seq_list.append(aa_seq)
#print aa_seq_list

structure_list = []
for topology in structure:
	strt = list(topology)
	#print strt
	structure_list.append(strt)
#print structure_list

"""
print aa_seq_list[0][5] #testing
print aa_seq_list[1][1] #testing 
print aa_seq_list[0][1] #testing and understanding
print structure_list[0][0] #testing and understanding
print structure_list[0][5] #testing and playing
"""

amino_acids_number = {'R':1, 'K':2, 'D':3, 'E':4, 'Q':5, 'N':6, 'H':7, 'S':8, 'T':9, 'Y':10, 'C':11, 'M':12, 'W':13, 'A':14, 'I':15, 'L':16, 'F':17, 'V':18, 'P':19, 'G':20}
#print len(amino_acids)

"""
#to get more output if necessary this would be a better alternative
for (slug, title) in aa_seq_list.items():
    print slug, title
"""


#creating the SVM format of sets; Set_0:


SVM = open(output_file, 'w+')
for (i, item) in enumerate(aa_seq_list): #run by sequences
	for (z, item2) in enumerate(item): #run by aa in sequence
		#position_aa =  str(amino_acids_number[aa_seq_list[i][z]])
		if structure_list[i][z] == 'S':
			#print aa_seq_list[i][z]
			#print structure_list[i][z]
			#print ' '
			print '+1 ', amino_acids_number[aa_seq_list[i][z]],':1'
			SVM.write('+1 ')
			SVM.write(str(amino_acids_number[aa_seq_list[i][z]]))
			SVM.write(':1')
			SVM.write('\n')

		else:
			print '-1 ', amino_acids_number[aa_seq_list[i][z]],':1'
			SVM.write('-1 ')
			SVM.write(str(amino_acids_number[aa_seq_list[i][z]]))
			SVM.write(':1')
			SVM.write('\n')
			


SVM.close()



