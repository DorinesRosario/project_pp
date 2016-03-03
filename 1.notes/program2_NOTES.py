


	###################### PROGRAM NOTES TASK 2: #################################

____________________________________________________________________________________________________

CDhit_list = []

with open('CDhit_headseq_file.txt', 'r') as file:
	lines = file.read().splitlines()
	
line_counter = 0
output_counter = 1 #?	
n = 60	
num_fileseq = (CDhit_list.items()[lines:lines+n] for lines in xrange(0, len(CDhit_list),n))
for line in lines:
	CDhit_list.append(line)
	for string in CDhit_list:
		if string[0] == '0' and num_fileseq <= 60:
			output_counter = output_counter + 1
			with open('prep_set_files{0}.txt'.format, 'w') as set_file:
				set_file.write(string)
		
print CDhit_list

____________________________________________________________________________________________________

seq_per_file = 1
file_num = 0
file_handle = ''
OutString = ''

for intemcount,keys in enumerate(head_sequence):
	OutString += '>{0}\n{1}\n'.format(keys,head_sequence[keys])
	if not intemcount % seq_per_file:
		if file_handle:
			file_handle.write(OutString)
			file_handle.close()
			OutString = ''
		file_num +=1
		file_info = 'input{0}.fasta'.format(file_num)
		file_handle = open (file_info, 'w')
file_handle.write(OutString)
file_handle.close()


____________________________________________________________________________________________________


with open('CDhit_headseq_file.txt', 'r') as file:
	lines = file.read().splitlines()
	for line in lines:
		CDhit_list.append(line)

#set up a way of creating new set_files by name --> loop along counters
line_counter = 0
outer_count = 1
if line[0] == '0':
	True
else:
	False
#sorting = True
while True:
	count = 0
	increment_set = (outer_count - 1) * 70
	left = len(CDhit_list) - increment_set
	set_file = 'prep_set_file' + str(outer_count * 70) + '.txt'

#to create the set_files with the correct lines --> nested loops inside previous loop
	new_set = []
	if left <= 70:
		while count < left:
			new_set.append(CDhit_list[line_counter])
			count += 1
			line_counter += 1
		line[0] == '0'
		#sorting = False
	else:
		while count <= 70:
			new_set.append(CDhit_list[line_counter])
			count += 1
			line_counter += 1

#last step !!: write the new file in the first loop and add the last counter increment, in this way the loop will go through again and write a new file
outer_count += 1
with open(set_file, 'w') as new_file:
	for row in new_set:
		new_file.write(row)


print CDhit_list
print new_set




____________________________________________________________________________________________________

prep_set_1 = []
prep_set_2 = []
prep_set_3 = []
prep_set_4 = []
prep_set_5 = []
prep_set_6 = []

#print prep_set_6, prep_set_5, prep_set_4, prep_set_3, prep_set_2, prep_set_1
____________________________________________________________________________________________________

with open('CDhit_headseq_file.txt', 'r') as file:
	lines = file.read().splitlines()
set_size = 60
counter = 1
set_file = open('prep_set_files.txt' %counter, 'w+')
for i,line in enumerate(file):
	f.write(line)
	if not i%set_size:
		set_file.close()
		file += 1
		set_file = open('prep_set_files.txt' %counter, 'w+')
	set_file.close()


____________________________________________________________________________________________________
#print line
	#CDhit_list.append(line)
	if line[0] == '0' and counter >= 60:
		counter = counter + 1
		prep_set_1.append(line)

____________________________________________________________________________________________________
def check(filename,linenumber):
    handel=open(filename,'r').readlines()

    return handel[linenumber-1][0]


cf=open('clusterfinal.txt','r').read().split('\n')
a=0
b=60
o1=''
for x in cf:
    if b<len(cf):
        if (b-a)>= 60 and check('clusterfinal.txt',b+1)== '0':
            o1=cf[a:b]
            print o1
            print len(o1)
            a=b
            b=b+60
            continue
        else:
            b=b+1

    else:
        o1=cf[a:len(cf)]
        print o1
        print len(o1)
        break


____________________________________________________________________________________________________

#import linecache
#import intertools
with open('cluster_results.clstr', 'r') as file:
	for line in file:
		row = line.strip()
		if row[0] in ['0', '1', '2', '3', '4']:
			print line.strip()
			print row[0]




clline=open('clusternohead.txt','r').readlines()
clusterfinal=open('clusterfinal.txt','w')
for i in clline:
    for x in range(len(i)):
        if i[x] == '>':
            clusterfinal.write(i[0])
            clusterfinal.write(' ')
            clusterfinal.write(i[x+1:x+5])
            clusterfinal.write('\n')
clusterfinal.close()


____________________________________________________________________________________________________
#import linecache
import intertools
with open('cluster_results.clstr', 'r') as file:
	lines = file.readlines()
	row_counter = 1
	for row in lines:
	#row = row.strip()
	#if '>Cluster' not in row:
		file_list = [row.strip.split() for row in intertools.ifilter(lambda row: row [0] not in '012', file)]
		#file_list = [row.strip.split() for row in file if (row[0] <> '0' and i[0] <> '1')]


print file_list


	if row[0] != '>':
			file_list.append([line.strip().split()])



____________________________________________________________________________________________________
import linecache
with open('cluster_results.clstr', 'r') as file:
	lines = file.readlines()
row_counter = 1
for row in lines:
	if row[0] == '0':
		True
		#for row in lines:
		if '>Cluster' not in row:
			if row[0] == True and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_1,append(row) 
				#row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_2,append(row)	
				#row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_3,append(row)
				#row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_4,append(row)
				#row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_5,append(row)
				#row_counter = 0
			elif row[0] == '0' and row_counter >= 70:
				row_counter = row_counter + 1
				prep_set_6,append(row)
				#row_counter = 0

print prep_set_6, prep_set_5, prep_set_4, prep_set_3, prep_set_2, prep_set_1





"""
#file.next() #to skip and not include clusters_head lines in my outputs

file_counter = 1
for line in file:
	if first_char == T and count >= 50:
		file_counter = file_counter + 1
		4

"""




____________________________________________________________________________________________________
	#import linecache
with open('cluster_results.clstr', 'r') as file:
	lines = file.readlines()
row_counter = 1
for row in lines:
	if row[0] == '0':
		True
	else:
		False
		#for row in lines:
		if '>Cluster' not in row:
			if row[0] == '0' and row_counter >= 50: #if there is a '0' as first character of the line  !!????!!
				row_counter = row_counter + 1
				prep_set_1,append(row) 
				row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_2,append(row)	
				row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_3,append(row)
				row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_4,append(row)
				row_counter = 0
			elif row[0] == '0' and row_counter >= 50:
				row_counter = row_counter + 1
				prep_set_5,append(row)
				row_counter = 0
			elif row[0] == '0' and row_counter >= 70:
				row_counter = row_counter + 1
				prep_set_6,append(row)
				row_counter = 0

print prep_set_6, prep_set_5, prep_set_4, prep_set_3, prep_set_2, prep_set_1