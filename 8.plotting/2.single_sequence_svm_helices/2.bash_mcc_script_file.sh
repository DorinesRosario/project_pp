#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_helices/
output_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_helices/

for file in $input_files/*.txt; do
	base=`basename $file .txt`
	python mcc_script.py $input_files/$base.txt $input_files/$base.pred.all $output_files/$base.mcc_allsets_helices.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt