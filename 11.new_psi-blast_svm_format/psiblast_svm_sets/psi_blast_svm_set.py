
import sys
import glob
import os


#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

#create svm set files considering CD-hit clustering for psi-blast
#________________________________________________________________



#list with the sequences_name by the same order as psi_blast svm format files
#____________________________________________________________________________

name_list = []

with open('sequences_name_list.txt', 'r') as seqs_name:
	names = seqs_name.read().splitlines()
for name in names:
	name_list.append(name)
seqs_name.close()
print name_list



#create lists of the 6 svm set files considering CD-hit clustering
#_________________________________________________________________

set_0 = []
set_1 = []
set_2 = []
set_3 = []
set_4 = []
set_5 = []

with open('prep_set_file0.txt', 'r') as set_file0:
	set0 = set_file0.read().splitlines()
for seqs0 in set0:
	set_0.append(seqs0)
set_file0.close()
print set_0


with open('prep_set_file1.txt', 'r') as set_file1:
	set1 = set_file1.read().splitlines()
for seqs1 in set1:
	set_1.append(seqs1)
set_file1.close()
print set_1


with open('prep_set_file2.txt', 'r') as set_file2:
	set2 = set_file2.read().splitlines()
for seqs2 in set2:
	set_2.append(seqs0)
set_file2.close()
print set_2


with open('prep_set_file3.txt', 'r') as set_file3:
	set3 = set_file3.read().splitlines()
for seqs3 in set3:
	set_3.append(seqs3)
set_file3.close()
print set_3


with open('prep_set_file4.txt', 'r') as set_file4:
	set4 = set_file4.read().splitlines()
for seqs4 in set4:
	set_4.append(seqs4)
set_file4.close()
print set_4


with open('prep_set_file5.txt', 'r') as set_file5:
	set5 = set_file5.read().splitlines()
for seqs5 in set5:
	set_5.append(seqs5)
set_file5.close()
print set_5



#input the psi-blast files in svm format and connect them with the respective seq_name using a dictionary
#________________________________________________________________________________________________________

psi_blast_list = []


"""
#testing the program
#___________________

psi_blast = open('sequence19.svm_format.txt', 'r').read()
psi_blast_list.append(str(psi_blast))
print psi_blast_list

psi_blast23 = open('sequence23.svm_format.txt', 'r').read()
psi_blast_list.append(str(psi_blast23))
print psi_blast_list
"""
"""
pathway_psi_blast_files = ('/home/rosario/Desktop/psiblast_svm_sets/prep_set_files/*.txt')
psi_blast_files = glob.glob(pathway_psi_blast_files)
for psi_blast_f in psi_blast_files:
	f_psi_blast = open(psi_blast_f, 'r').read().splitlines()
	psi_blast_list.append(str(psi_blast_f))
	#psi_blast_f.close()
"""

os.chdir('/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step4/')         
for file in list(glob.glob('*.txt')):                                       
    reader = open(file, 'r').read()
    psi_blast_list.append(str(reader))

print '*************************', psi_blast_list



#dictionary = {seq_name : psi-blast_svm_format}
#______________________________________________

keys = name_list
values = psi_blast_list
stride_database = dict(zip(keys, values))
print stride_database


print 'psi_blas_list len:', len(psi_blast_list)
print 'stride_database len:', len(stride_database)
print stride_database.keys()



#create a for loop over the set_cluster lists to distribute the psi-blast files by C-hit clustering
#__________________________________________________________________________________________________

svm_set0 = []
svm_set1 = []
svm_set2 = []
svm_set3 = []
svm_set4 = []
svm_set5 = []


for keys, values in stride_database.iteritems():
	print keys
	if keys in set_0:
		svm_set0.append(stride_database[keys])
	elif keys in set_1:
		svm_set1.append(stride_database[keys])
	elif keys in set_2:
		svm_set2.append(stride_database[keys])
	elif keys in set_3:
		svm_set3.append(stride_database[keys])
	elif keys in set_4:
		svm_set4.append(stride_database[keys])
	elif keys in set_5:
		svm_set5.append(stride_database[keys])


print 'svm set 0:', svm_set0
print 'svm set 1:', svm_set1
print 'svm set 2:', svm_set2
print 'svm set 3:', svm_set3
print 'svm set 4:', svm_set4
print 'svm set 5:', svm_set5


#write set files for psi-blast in svm format:
#____________________________________________


with open('psi_blast_svm_set0.txt', 'w') as svm_file0:
	for psi_blast_svm in svm_set0:
		svm_file0.write(psi_blast_svm)
		svm_file0.write('\n')
svm_file0.close()


with open('psi_blast_svm_set1.txt', 'w') as svm_file1:
	for psi_blast_svm in svm_set1:
		svm_file1.write(psi_blast_svm)
		svm_file1.write('\n')
svm_file1.close()


with open('psi_blast_svm_set2.txt', 'w') as svm_file2:
	for psi_blast_svm in svm_set2:
		svm_file2.write(psi_blast_svm)
		svm_file2.write('\n')
svm_file2.close()


with open('psi_blast_svm_set3.txt', 'w') as svm_file3:
	for psi_blast_svm in svm_set3:
		svm_file3.write(psi_blast_svm)
		svm_file3.write('\n')
svm_file3.close()


with open('psi_blast_svm_set4.txt', 'w') as svm_file4:
	for psi_blast_svm in svm_set4:
		svm_file4.write(psi_blast_svm)
		svm_file4.write('\n')
svm_file4.close()


with open('psi_blast_svm_set5.txt', 'w') as svm_file5:
	for psi_blast_svm in svm_set0:
		svm_file5.write(psi_blast_svm)
		svm_file5.write('\n')
svm_file5.close()