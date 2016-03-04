#code for Task2: CREATE CROSS-VALIDATION SETS:
#the clusters from CD-hit should be randomly distribuited by the created sets; homologs sequences cannot be separeted in different sets;



#from the output obtained by CD-hit website, create 6 pre_set files 
#6 pre-sets: based on homology btw seq from CD-hit clustering
#through dictionary and homology_set_lists create 6 set files with: head_sequence, aa_sequence and structure


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


CDhit_headseq.close()


#def initial_position(line):
#	
#	if line[0] == '0':
#		return True
#	else:
#		return False

#def test_initial_position(line):
#	assert initial_position0(line[0] == '0') == True
#	assert initial_position0(line[0] != '0') == False


f = open('CDhit_seq_name.txt', 'r')

new_file_size = 0
num_set_files = 0
set_file = open ('prep_set_file'+str(num_set_files)+'.txt', 'w+')

for line in f:
	#initial_position(line)
	#print line
	#print initial_position(line)
	if line.startswith('0') and new_file_size >= 60:
			set_file.close()
			num_set_files = num_set_files + 1
			set_file = open ('prep_set_file'+str(num_set_files)+'.txt', 'w+')
			set_file.write(line)
			new_file_size = 0
			#print line
			

	else:
		set_file.write(line)
		new_file_size += 1
		#print line
		
set_file.close()
print 'done!!!'
