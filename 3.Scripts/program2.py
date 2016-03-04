#code for Task2: CREATE CROSS-VALIDATION SETS:
#the clusters from CD-hit should be randomly distribuited by the created sets; homologs sequences cannot be separeted in different sets;


#create a dictionaty from the dataset file in which: {key(head_seq): value(aa_sequence), value(structure)}



head_sequence = []
aa_sequence = [] 
structure = [] 

import linecache
#with open('stride.3line', 'r') as file:
with open('test_stride.txt', 'r') as file:
	lines = file.read().splitlines()
line = 1

dataset_seqs = {}
for line in range(0, int(len(lines)),3):
	dataset_seqs[lines[line]] = (lines[line + 1], lines[line + 2])

#print dataset_seqs



#from the output obtained by CD-hit website, create 6 pre_set files 
#6 pre-sets: based on homology btw seq from CD-hit clustering
#through dictionary and homology_set_lists create 6 set files with: head_sequence, aa_sequence and structure


with open('cluster_results.clstr', 'r') as file:
	CDhit_headseq = open('CDhit_headseq_file.txt', 'w+')
	for line in file:
		row = line.strip()
		if row[0] in ['0', '1', '2', '3', '4']:
			for char in range(len(row)):
				if row[char] == ',':
					CDhit_headseq.write(row[0])
					CDhit_headseq.write(' ')
					CDhit_headseq.write(row[char+2:char+7])
					CDhit_headseq.write('\n')
CDhit_headseq.close()




def initial_position(line):
	
	if line[0] == '0':
		return True
	else:
		return False

def test_initial_position(line):
	assert initial_position0(line[0] == '0') == True
	assert initial_position0(line[0] != '0') == False


CDhit_list = []

f = open('CDhit_headseq_file.txt', 'r')
	#lines = f.read().splitlines()
new_file_size = 0
num_set_files = 0
set_file = open ('prep_set_file'+str(num_set_files)+'.txt', 'w+')

for line in f:
	initial_position(line)
	#print initial_position(line)
	if line.startswith('0') and new_file_size >= 60:
			#line_counter = line_counter + 1
			set_file = open ('prep_set_file'+str(num_set_files)+'.txt', 'w+')
			set_file.write(line)
			new_file_size = 0
			num_set_files = num_set_files + 1
			#set_file.write(line)


	else:
		#line_counter = line_counter + 1
		set_file.write(line)
		new_file_size += 1
		#new_file_size = new_file_size + 1
print 'done!!!'

