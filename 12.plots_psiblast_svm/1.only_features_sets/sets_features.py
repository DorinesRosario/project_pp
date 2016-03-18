"""
import sys

datasets = sys.argv[1]
features_s = sys.argv[2]
"""
dataset = open ('psi_blast_set6.svm', 'r').readlines()
features = open ('psi_blast_set6.features', 'w+')
for lines in dataset:
	#print lines[0:2]
	features.write(lines[0:2])
	features.write('\n')