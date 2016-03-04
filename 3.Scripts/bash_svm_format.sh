#!/bin/bash
sets_input_dir_files=/home/rosario/Desktop/project_pp/4.SingleSeq_sets/3.set_files/
svm_output_dir_files=/home/rosario/Desktop/project_pp/4.SingleSeq_sets/4.svm_sinseq_files/


for file in $sets_input_dir_files/*.txt; do
	base=`basename $file .txt`
	python program_svm_format.py $file $svm_output_dir_files/$base.svm


done