import math
import sys

svm_set = sys.argv[1]
pred_set = sys.argv[2]
mcc_op = sys.argv[3]


TP = 0
TN = 0
FP = 0
FN = 0

svm_set_file = open(sys.argv[1], 'r').read().splitlines()
pred_set_file = open(sys.argv[2], 'r').read().splitlines()

for row in range(len(svm_set_file)):
	if svm_set_file[row][:2] == '+1' and float(pred_set_file[row]) > 0:
		TP = TP + 1
	if svm_set_file[row][:2] == '+1' and float(pred_set_file[row]) < 0:
		FP = FP + 1
	if svm_set_file[row][:2] == '-1' and float(pred_set_file[row]) < 0:
		TN = TN + 1
	if svm_set_file[row][:2] == '-1' and float(pred_set_file[row]) > 0:
		FN = FN + 1
mcc_output = open (sys.argv[3], 'w')
print ((TP * TN - FP * FN) / math.sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) ))
print format(float((TP + TN))/float((TP + TN + FP + FN)),'2%')
mcc_output.write('TP:')
mcc_output.write('\n')
mcc_output.write(str(TP))
mcc_output.write('\n')
mcc_output.write('\n')
mcc_output.write('FP:')
mcc_output.write('\n')
mcc_output.write(str(FP))
mcc_output.write('\n')
mcc_output.write('\n')
mcc_output.write('TN:')
mcc_output.write('\n')
mcc_output.write(str(TN))
mcc_output.write('\n')
mcc_output.write('\n')
mcc_output.write('FN:')
mcc_output.write('\n')
mcc_output.write(str(FN))
mcc_output.write('\n')
mcc_output.write('\n')
mcc_output.write('MCC:')
mcc_output.write('\n')
mcc_output.write('(TP * TN - FP * FN) /( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )')
mcc_output.write('\n')
mcc_output.write(str((TP * TN - FP * FN) / math.sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )))
mcc_output.write('\n')
mcc_output.write('\n')
mcc_output.write('Accuracy:')
mcc_output.write('\n')
mcc_output.write('(TP + TN)/(TP + TN + FP + FN)')
mcc_output.write('\n')
mcc_output.write(str(format(float((TP + TN))/float((TP + TN + FP + FN)),'2%')))
