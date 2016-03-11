#!/bin/bash
sets_input_dir_files=/home/rosario/Desktop/project_pp/10.sing_seq_helices/1.sing_seq_sets/
svm_output_dir_files=/home/rosario/Desktop/project_pp/10.sing_seq_helices/2.svm_helices_sets/


for file in $sets_input_dir_files/*.txt; do
	base=`basename $file .txt`
	python program1_svm_format_helices.py $file $svm_output_dir_files/$base.svm


done