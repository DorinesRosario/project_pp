#program notes

amino_acids = ['R', 'K', 'D', 'E', 'Q', 'N', 'H', 'S', 'T', 'Y', 'C', 'M', 'W', 'A', 'I', 'L', 'F', 'V', 'P', 'G']
#print len(amino_acids)


with open('test_stride.txt', 'r') as file:

dataset = {}
dataset['head_seq'] = first line
dataset['aa_seq'] = second line
dataset['structure'] = third line
	# o que eu quero é que head_seq seja key e aaseq e structure sejam values

with open('test_stride.txt', 'r') as file:
	for line in file:
		if '>' in line: # '>' only present in the head of the sequence
			head_sequences.append(line)
		if '>' not in line:
			if 'M' in line: # Methionine ('M') is the only 
				aa_sequeces.append(line)
			if 'M' not in line(line)
				structure.append
	print head_sequences, aa_sequeces, structure

_________________________________________________________________________________

with open('test_stride.txt', 'r') as file:
	lines = file.readlines()
dict = {}
current_key = None
for line in lines:
	line = line.strip()

	if '>' not in line:
		current_key = None
	elif not current_key:
		current_key = line
		dict[current_key] = []
	else:
		dict[current_key].append(line)

print dict

_________________________________________________________________________________with open('test_stride.txt', 'r') as file:
	lines = file.readlines()
dict = {}
sequence = None
for line in lines:
	line = line.strip()
	#sequence, features = line[0], line[1:0] 
	if '>' in line:
		sequence = line
	elif '>' not in line:
			dict[sequence] = []
			#dict[sequence].append(line)
	else:	
		dict.setdefault(sequence, []).append(line)
print dict

______________________________________________________________

from collections import defaultdict
d = defaultdict(list)

with open('test_stride.txt', 'r') as file:
	for line in file:
		if '>' in line:
			k, v = line.rstrip().split(':')
			d[k].extend(map(str.strip,v.split(':')) if v.strip() else [])
		else:
			d[k].append(line.rstrip())

print (d)

_________________________________________________________________________________

ACTUAL:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()
dict = {}
sequence = None
features = []
for line in lines:
	line = line.strip()
	#sequence, features = line[0], line[1:0] 
	if '>' in line:
		sequence = line
	else:
		if '>' not in line:
			dict[sequence] = []
			#dict[sequence].append(line)
			dict.setdefault(sequence).append(line)
print dict
________________________________________________________________-

for a in range(3):

________________________________________________________________

for i in range(len(a)):
...     print a[i]

LINKS:

https://en.wikipedia.org/wiki/Hash_table
https://docs.python.org/2/tutorial/datastructures.html
https://docs.python.org/2/tutorial/controlflow.html#defining-functions
https://docs.python.org/2/tutorial/controlflow.html
https://docs.python.org/2/tutorial/introduction.html#strings
_________________________________________________________________________________


for string in seq_and_struc:
	for char in string:
		if char in list:
			aa_sequeces.append(string)
		if char not in list:
			structures.append(string)

print 'aa sequences:', '\n', '\n', aa_sequeces, '\n', '\n', 'Topology structures:', '\n', '\n', structures
print 'aa_sequeces:', len(aa_sequeces), 'structures:', len(structures)

_________________________________________________________________________________

amino_acids = ['R', 'K', 'D', 'E', 'Q', 'N', 'H', 'S', 'T', 'Y', 'C', 'M', 'W', 'A', 'I', 'L', 'F', 'V', 'P', 'G']
#print len(amino_acids)
aa_feature = ['S', 'C', 'H']
list = ['R', 'K', 'D', 'E', 'Q', 'N', 'T', 'Y', 'M', 'W', 'A', 'I', 'L', 'F', 'V', 'P', 'G']

head_sequences = []
aa_sequeces = []
structures = []
seq_and_struc = []

#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()

for line in lines:
	line = line.strip()
	if '>' in line:
		head_sequences.append(line)
	if '>' not in line:
		seq_and_struc.append(line)


print 'Head sequences:', '\n', '\n', head_sequences, '\n', '\n', 'aa sequences and structures:', '\n', '\n', seq_and_struc
print 'head_sequences:', len(head_sequences), 'aa sequences and structures:', len(seq_and_struc)
_______________________________________________________________________________

amino_acids = ['R', 'K', 'D', 'E', 'Q', 'N', 'H', 'S', 'T', 'Y', 'C', 'M', 'W', 'A', 'I', 'L', 'F', 'V', 'P', 'G']
#print len(amino_acids)
aa_feature = ['S', 'C', 'H']
list = ['R', 'K', 'D', 'E', 'Q', 'N', 'T', 'Y', 'M', 'W', 'A', 'I', 'L', 'F', 'V', 'P', 'G']

head_sequences = []
aa_sequeces = []
structures = []
seq_and_struc = []

#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()

for line in lines:
	n = 0
	line = line.strip()
	if '>' in line:
		n = n + 1
		head_sequences.append(line)
	if '>' not in line:
		for n + 2:
			aa_sequeces.append(line)
		for n + 3:
			structures.append(line)


#print 'Head sequences:', '\n', '\n', head_sequences, '\n', '\n', 'aa sequences and structures:', '\n', '\n', seq_and_struc
#print 'head_sequences:', len(head_sequences), 'aa sequences and structures:', len(seq_and_struc)
print 'head_sequences:', len(head_sequences), 'aa_sequeces:', len(aa_sequeces), 'structures:', len(structures)

_________________________________________________________________________________

READ AND WRITE FILES:

http://www.tutorialspoint.com/python/file_writelines.htm
http://opentechschool.github.io/python-data-intro/core/text-files.html
http://pythoncentral.io/reading-and-writing-to-files-in-python/

_________________________________________________________________________________

Strings, Lists, Arrays, and Dictionaries:

http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html

_________________________________________________________________________________

NOTES:
#code for Task1: EXTRACT FEATURES FROM DATABASE: 
#features that are positive/negative examples for my predicter(beta_sheets)

amino_acids_number = {'R':1, 'K':2, 'D':3, 'E':4, 'Q':5, 'N':6, 'H':7, 'S':8, 'T':9, 'Y':10, 'C':11, 'M':12, 'W':13, 'A':14, 'I':15, 'L':16, 'F':17, 'V':18, 'P':19, 'G':20}
#print len(amino_acids)

head_sequence = []
aa_sequence = [] 
structure = [] 


import linecache
#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.readlines()
head_sequence_file = open('head_sequence_file.txt', 'w+')
aa_sequence_file = open('aa_sequence_file.txt', 'w+')
structure_file = open('structure_file.txt', 'w+')

line = 1
for row in lines:
	row = row.strip()
	if (line%3 == 1):
		head_sequence_file.write(row)
		line = line + 1
		head_sequence.append(row)
	elif (line%3 == 2):
		aa_sequence_file.write(row)
		line = line + 1
		aa_sequence.append(row)
	elif (line%3 == 0):
		structure_file.write(row)
		line = line + 1
		structure.append(row)

# note: !!it is adding the rows in the files without space btw them!! to have new lines: write file from lists
head_sequence_file.close()
aa_sequence_file.close()
structure_file.close()


print 'Head sequence:', '\n', '\n', head_sequence, '\n', '\n', 'aa sequence:', '\n', '\n', aa_sequence, '\n', '\n', 'topology structure:', '\n', '\n', structure
print 'head_sequence:', len(head_sequence), 'aa_sequece:', len(aa_sequence), 'structure:', len(structure)


"""
#to break my sequences into char, array, to then evaluate and study correspondent ones
structure_list = list(structure)
aa_sequence_list = list(aa_sequence)
print structure_list, aa_sequence_list
"""

#{seq1:str1, seq2:str2, seq3:str3 ...}; I want char by char {char1seq1:char1str1, char2seq1:char2str1 ...}
aa_seq_list = []
for sequence in aa_sequence:
	aa_seq = list(sequence)
	#print aa_seq
	aa_seq_list.append(aa_seq)
print aa_seq_list

structure_list = []
for topology in structure:
	strt = list(topology)
	#print strt
	structure_list.append(strt)
print structure_list

#Map aa_seq_list[] and structure_list[] into a dictionary 
dictionary = dict(zip (aa_seq_list, structure_list))
print dictionary
 



"""
#array = {'A', 'B'} same as [0:'A', 0:'B'] --> aa_sequence_list[0] ~ structure_list[0]
array = [aa_sequence_list, structure_list] #with {} error: unhashable type:'list'
for [i] in array:
	if 'S' in [structure_list]:
		print '+1 ', amino_acids_number[aa_sequence_list], ':1' #to print the respective amino_acid_number of the aa present in the aa_sequence in this position
	if 'C' in [structure_list]:
		print '-1 ', amino_acids_number[aa_sequence_list], ':1'
	if 'H' in [structure_list]:
		print '-1 ', amino_acids_number[aa_sequence_list], ':1'
"""

_________________________________________________________________________________

for key in dict.iterkeys(): ...

for value in dict.itervalues(): ...

for key, value in dict.iteritems(): ...

_________________________________________________________________________________


"""
for tuple_aa_seq_list, tuple_structure_list in seq_database.items():
	#for i in tuple_aa_seq_list:
#for sequence in seq_database.tuple_aa_seq_list(tuple_structure_list):	
	if 'S' in tuple_structure_list:
		print '+1 ', amino_acids_number[tuple_aa_seq_list], ':1', '\n'
	elif 'C' in tuple_structure_list:
		print '-1 ', amino_acids_number[tuple_aa_seq_list], ':1', '\n'
	elif 'H' in tuple_structure_list:
		print '-1 ', amino_acids_number[tuple_aa_seq_list], ':1', '\n'
	"""
