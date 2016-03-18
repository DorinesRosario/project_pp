#sorting the file with features and predictions by predictions 
"""
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
"""

sort_file = open ('k5.svm.roc_step1.txt', 'r').read().splitlines()
step2_file = open ('k5.sorted', 'w+')
for lines in sorted(sort_file, key=lambda line:float(line.split()[1])):
	step2_file.write(lines + '\n')

step2_file.close()