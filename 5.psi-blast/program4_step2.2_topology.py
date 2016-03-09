#TASK 4: ADD EVOLUTIONARY INFORMATION BY RUNNING PSI-BLAST AND EXTRACTING THE INFORMATION

import sys


#transform topology structure of the sequence into positive/negative examples
#____________________________________________________________________________

topology = []

input_file = sys.argv[1]
output_file = sys.argv[2]

structure_file = open(input_file, 'r').read().splitlines()
for line in structure_file:
	print line
	topology.append(line)

print topology


topology_list = []
for top in topology:
	strct = list(top)
print strct
topology_list.append(strct)
#print topology_list


features = {'S':'+1 ', 'H':'-1 ', 'C':'-1 '}

seq_topology = []

features_file = open(output_file, 'w')

for feature in strct:
	print features[feature]
	seq_topology.append(features [feature])
	features_file.write(features [feature])
	features_file.write('\n')
print seq_topology










