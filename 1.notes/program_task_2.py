#program task 2

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
