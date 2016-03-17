

dataset = open ('all.svm.helices', 'r').readlines()
features = open ('helices.features.txt', 'w+')
for lines in dataset:
	#print lines[0:2]
	features.write(lines[0:2])
	features.write('\n')