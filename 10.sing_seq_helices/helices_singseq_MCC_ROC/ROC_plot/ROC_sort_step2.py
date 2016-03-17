#sorting the file with features and predictions by predictions 

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


sort_file = open (input_file, 'r').read().splitlines()
step2_file = open (output_file, 'w+')
for lines in sorted(sort_file, key=lambda line:float(line.split()[1])):
	step2_file.write(lines + '\n')

step2_file.close()