


file_set_svm = open ('final_set_file5.svm', 'r').read().splitlines()

line = 1
dataset = open('dataset_features_set5.txt', 'w' )
for feature in file_set_svm:
	dataset.write(feature[0:2])
	dataset.write('\n')

file_set_svm.close()
dataset.close()