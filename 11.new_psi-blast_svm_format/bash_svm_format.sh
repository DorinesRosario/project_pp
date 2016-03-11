#!/bin/bash
sets_input_dir_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_output/
svm_output_dir_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step1/


for file in $sets_input_dir_files/*.psi; do
	base=`basename $file .psi`
	python program4_step1_transform_psi-blast_output.py $file $svm_output_dir_files/$base.svm


done