#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/mcc_sig_seq_lineark/
output_files=/home/rosario/Desktop/project_pp/8.plotting/mcc_sig_seq_lineark/

for file in $input_files/*.svm; do
	base=`basename $file .svm`
	python mcc_singseq_lineark.py $input_files/$base.svm $input_files/$base.svm.pred $output_files/$base.mcc_lineark.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt