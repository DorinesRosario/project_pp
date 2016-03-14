#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_j2.35/MCC_sing_seq_set_by_set/
output_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_j2.35/MCC_sing_seq_set_by_set/

for file in $input_files/*.svm0.pred; do
	base=`basename $file .svm0.pred`
	python mcc_script.py $input_files/$base.txt $input_files/$base.svm0.pred $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt