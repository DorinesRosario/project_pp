
import sys

datasets = sys.argv[1]
features_s = sys.argv[2]

dataset = open (datasets, 'r').readlines()
features = open (features_s, 'w+')
for lines in dataset:
	#print lines[0:2]
	features.write(lines[0:2])
	features.write('\n')